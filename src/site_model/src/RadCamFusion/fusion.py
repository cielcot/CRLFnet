#!/usr/bin/env python3

"""
Get the radar and camera messages and do Radar-camera fusion.
"""


from time import perf_counter, sleep
from pathlib import Path
import argparse
import yaml
import numpy as np

import cv2
from cv_bridge import CvBridge

import rospy
import message_filters
from sensor_msgs.msg import Image               # Camera message
from msgs.msg._MsgRadar import MsgRadar         # Radar message
from msgs.msg._MsgRadCam import MsgRadCam       # fusion message

from ..utils.poi_and_roi import radar_poi, image_roi, expand_poi, optimize_iou
from ..utils.kalman import *
from ..utils.yolo.yolo import YOLO
from ..utils.visualization import radar2visual  # visualized output


def residual(uir, uii):
    ri = np.concatenate((np.expand_dims(uir, 1), np.full((uir.size, 1), -1)), axis=1)
    ii = np.concatenate((np.full((uii.size, 1), -1), np.expand_dims(uii, 1)), axis=1)
    return ri, ii


def pair_fusion(radar: MsgRadar, image: Image, w2c: np.ndarray, c2p: np.ndarray, name: str):
    # ONLY FUSE THE LEFT PAIR!!!
    global yolo
    global state_xpt_pile, state_cov_pile
    global w2cs, c2ps
    global frame_counter, my_timer
    global max_id

    # Info
    my_now = perf_counter()
    del_time = my_now - my_timer
    print("\033[1;36m\"{}\", FPS: {:.2f}, Frame {}\033[0m".format(name, 1.0 / del_time, frame_counter))
    frame_counter += 1
    my_timer = my_now

    # Separate Decection
    print("\033[1;36mSeparate Detection\033[0m")
    # acquire radar POIs in pixel coordinate and the observation vectors
    # poi = (u, v, 1), dtype=int;  z = (distance, angle, velocity)
    radar_pois, radar_zs = radar_poi(radar.objects_left, w2c, c2p, image.width, image.height)
    radar_obj_num = len(radar_pois)
    # acquire image ROIs in pixel coordinate and the observation vectors
    # roi = (left, top, right, bottom, score, class), dtype=int;  z = (u, v)
    image_rois= image_roi(image, yolo)
    image_zs = np.concatenate(((image_rois[:, 0:1] + image_rois[:, 2:3]) // 2,
                               (image_rois[:, 1:2] + 3 * image_rois[:, 3:4]) // 4),
                                axis=1)
    image_obj_num = len(image_rois)
    # print results
    print("Radar POIs (pixel):\t", radar_pois)
    print("Radar obs vectors:\t", radar_zs)
    print("Image ROIs (pixel):\t", image_rois)
    print("Image obs vectors:\t", image_zs)

    # Fusion
    print("\033[1;36mFusion\033[0m")
    # IOU matching of radar and image ROIs
    radar_expanded_rois = np.array(list(map(lambda p, d: expand_poi(p, d, image.width, image.height),
                                            radar_pois, radar_zs[:, 0])),
                                            dtype=int)
    print("Radar expanded ROIs:\t", radar_expanded_rois)
    match_pairs = optimize_iou(radar_expanded_rois, image_rois)
    print("matched pairs:", match_pairs)
    # residual algorithm (NOT finished)
    radar_indices, image_indices = (np.setdiff1d(np.arange(radar_obj_num), match_pairs[0]),
                                    np.setdiff1d(np.arange(image_obj_num), match_pairs[1]))
    print("unmatched indices:", "radar:", radar_indices, "image:", image_indices)
    """
    residual_pairs = residual(radar_indices, image_indices)
    print("residual pairs:", "radar:", residual_pairs[0], "image:", residual_pairs[1])
    """
    # generate possible object observation vectors
    zms = np.concatenate((radar_zs[match_pairs[0], 0:3], image_zs[match_pairs[1], 0:2]), axis=1)
    zrs = radar_zs[radar_indices, 0:3]
    zis = image_zs[image_indices, 0:2]
    # EKF
    # state_xpt = (Xw, Yw, Vx, Vy, age, id)
    A = np.array([[1, 0, del_time, 0], [0, 1, 0, del_time], [0, 0, 1, 0], [0, 0, 0, 1]])
    pred_xpt_pile, pred_cov_pile = bulk_predict(state_xpt_pile, state_cov_pile, A)
    exist_idx, lost_idx, new_idx = bulk_comparison(pred_xpt_pile, zms, zrs, zis, w2c, c2p)
    print("Exist Indices:\t", exist_idx)
    print("Lost Indices:\t", lost_idx)
    print("New Indices:\t", new_idx)
    bulk_update(exist_idx, pred_xpt_pile, pred_cov_pile, zms, zrs, zis, w2c, c2p)
    bulk_lost(lost_idx, state_xpt_pile, state_cov_pile)
    max_id = bulk_new(new_idx, state_xpt_pile, state_cov_pile, zms, zrs, zis, max_id)

    # Save Images
    if args.save and radar_obj_num !=0 and image_obj_num != 0:
        radar2visual(OUTPUT_DIR, image, radar_pois=radar_pois, radar_rois=radar_expanded_rois, image_rois=image_rois, appendix='Test')
    
    # Publish
    print("states:", state_xpt_pile)


def fusion(radar: MsgRadar, image2: Image, image3: Image):
    print('+------------------------+')
    pair_fusion(radar, image2, w2cs['camera2'], c2ps['camera2'], 'camera2')
    # pair_fusion(radar, image3, 'camera3')


if __name__ == '__main__':
    # fps counter
    my_timer = 0
    frame_counter = 0

    # storage of Kalman Filter
    max_id = 0
    state_xpt_pile = []     # (Xw, Yw, Vxw, Vyw, status, index)
    state_cov_pile = []     # covariance matrices

    # set command arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--off-yolo",
                        action      = 'store_true',
                        default     = False,
                        required    = False,
                        help        = "Disable yolo, save radar POIs and images per frame instead."
    )
    parser.add_argument("--fps",
                        type        = float,
                        default     = 2,
                        required    = False,
                        help        = "Approximate virtual fps."
    )
    parser.add_argument("-s", "--save",
                        action      = 'store_true',
                        default     = False,
                        required    = False,
                        help        = "Save visualized POIs and ROIs as images."
    )
    parser.add_argument("-t", "--trigger",
                        choices     = ['match', 'both', 'either', 'anyway'],
                        type        = str,
                        default     = 'match',
                        required    = False,
                        help        = "When to save images."
    )
    args = parser.parse_args()

    # get root path
    ROOT_DIR = Path(__file__).resolve().parents[2]
    # load config file
    CONFIG_DIR = ROOT_DIR.joinpath("config/config.yaml")
    with open(CONFIG_DIR, 'r') as f:
        try:
            config = yaml.load(f, Loader=yaml.FullLoader)
        except:
            print("\033[1;31mFailed to load config file.\033[0m")
            exit(1)
    OUTPUT_DIR = ROOT_DIR.joinpath(config['output']['RadCamFusion_dir'])
    MEASUREMENT_DIR = ROOT_DIR.joinpath(config['measurement']['measurement_dir'], 'measurement.txt')
    # load measurement file
    camera_index = {'camera11': 0, 'camera12': 1, 'camera13': 2, 'camera14': 3,
                    'camera2' : 4, 'camera3' : 5,
                    'camera41': 6, 'camera42': 7, 'camera43': 8, 'camera44': 9}
    measurement = np.loadtxt(MEASUREMENT_DIR)
    w2cs, c2ps = {}, {}
    for c in camera_index.keys():
        w2cs[c] = measurement[camera_index[c]][0:16].reshape(4, 4)
        c2ps[c] = measurement[camera_index[c]][16:28].reshape(3, 4)
    del measurement

    # initialize YOLO
    if not args.off_yolo:
        yolo = YOLO(ROOT_DIR, cuda=False)
        print("\033[0;32mYOLO initialized successfully.\033[0m")
    else:
        yolo = None
        print("\033[0;33mRunning in off-YOLO mode.\033[0m")
        OUTPUT_DIR = OUTPUT_DIR.joinpath("off_yolo")
        OUTPUT_DIR.mkdir(exist_ok=True)
    
    # initialize publisher
    pub = rospy.Publisher("/radar_camera_fused", MsgRadCam, queue_size=10)
    # initialize ROS node
    rospy.init_node('radar_camera_fusion', anonymous=True)
    # subscribe messages
    msg_radar   = message_filters.Subscriber('/radar_msgs_combined', MsgRadar)
    msg_image_2 = message_filters.Subscriber('/image_raw_2', Image)
    msg_image_3 = message_filters.Subscriber('/image_raw_3', Image)
    # syncronize time stamps
    sync = message_filters.ApproximateTimeSynchronizer([msg_radar, msg_image_2, msg_image_3], 1, 1)

    sync.registerCallback(fusion)

    print("\033[0;32mRadar-camera Fusion Initialized Sucessfully.\033[0m")

    rospy.spin()
