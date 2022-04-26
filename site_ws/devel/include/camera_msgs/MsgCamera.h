// Generated by gencpp from file camera_msgs/MsgCamera.msg
// DO NOT EDIT!


#ifndef CAMERA_MSGS_MESSAGE_MSGCAMERA_H
#define CAMERA_MSGS_MESSAGE_MSGCAMERA_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <camera_msgs/MsgObject.h>

namespace camera_msgs
{
template <class ContainerAllocator>
struct MsgCamera_
{
  typedef MsgCamera_<ContainerAllocator> Type;

  MsgCamera_()
    : header()
    , camera()  {
    }
  MsgCamera_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , camera(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector< ::camera_msgs::MsgObject_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::camera_msgs::MsgObject_<ContainerAllocator> >::other >  _camera_type;
  _camera_type camera;





  typedef boost::shared_ptr< ::camera_msgs::MsgCamera_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::camera_msgs::MsgCamera_<ContainerAllocator> const> ConstPtr;

}; // struct MsgCamera_

typedef ::camera_msgs::MsgCamera_<std::allocator<void> > MsgCamera;

typedef boost::shared_ptr< ::camera_msgs::MsgCamera > MsgCameraPtr;
typedef boost::shared_ptr< ::camera_msgs::MsgCamera const> MsgCameraConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::camera_msgs::MsgCamera_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::camera_msgs::MsgCamera_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::camera_msgs::MsgCamera_<ContainerAllocator1> & lhs, const ::camera_msgs::MsgCamera_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.camera == rhs.camera;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::camera_msgs::MsgCamera_<ContainerAllocator1> & lhs, const ::camera_msgs::MsgCamera_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace camera_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::camera_msgs::MsgCamera_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::camera_msgs::MsgCamera_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::camera_msgs::MsgCamera_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::camera_msgs::MsgCamera_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::camera_msgs::MsgCamera_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::camera_msgs::MsgCamera_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::camera_msgs::MsgCamera_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3fabcdea7625c1fd8242127e85ce45f6";
  }

  static const char* value(const ::camera_msgs::MsgCamera_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3fabcdea7625c1fdULL;
  static const uint64_t static_value2 = 0x8242127e85ce45f6ULL;
};

template<class ContainerAllocator>
struct DataType< ::camera_msgs::MsgCamera_<ContainerAllocator> >
{
  static const char* value()
  {
    return "camera_msgs/MsgCamera";
  }

  static const char* value(const ::camera_msgs::MsgCamera_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::camera_msgs::MsgCamera_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"MsgObject[] camera\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: camera_msgs/MsgObject\n"
"# This message contains an uncompressed image\n"
"# (0, 0) is at top-left corner of image\n"
"#\n"
"\n"
"Header header        # Header timestamp should be acquisition time of image\n"
"                     # Header frame_id should be optical frame of camera\n"
"                     # origin of frame should be optical center of camera\n"
"                     # +x should point to the right in the image\n"
"                     # +y should point down in the image\n"
"                     # +z should point into to plane of the image\n"
"                     # If the frame_id here and the frame_id of the CameraInfo\n"
"                     # message associated with the image conflict\n"
"                     # the behavior is undefined\n"
"\n"
"uint32 height         # image height, that is, number of rows\n"
"uint32 width          # image width, that is, number of columns\n"
"\n"
"# The legal values for encoding are in file src/image_encodings.cpp\n"
"# If you want to standardize a new string format, join\n"
"# ros-users@lists.sourceforge.net and send an email proposing a new encoding.\n"
"\n"
"string encoding       # Encoding of pixels -- channel meaning, ordering, size\n"
"                      # taken from the list of strings in include/sensor_msgs/image_encodings.h\n"
"\n"
"uint8 is_bigendian    # is this data bigendian?\n"
"uint32 step           # Full row length in bytes\n"
"uint8[] data          # actual matrix data, size is (step * rows)\n"
;
  }

  static const char* value(const ::camera_msgs::MsgCamera_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::camera_msgs::MsgCamera_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.camera);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MsgCamera_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::camera_msgs::MsgCamera_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::camera_msgs::MsgCamera_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "camera[]" << std::endl;
    for (size_t i = 0; i < v.camera.size(); ++i)
    {
      s << indent << "  camera[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::camera_msgs::MsgObject_<ContainerAllocator> >::stream(s, indent + "    ", v.camera[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // CAMERA_MSGS_MESSAGE_MSGCAMERA_H
