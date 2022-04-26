# Install script for directory: /home/zonlin/IPP_WorkSpace/ROS_WS/site_ws/src/ARS_gazebo_plugin/radar_plugin

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/zonlin/IPP_WorkSpace/ROS_WS/site_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/zonlin/IPP_WorkSpace/ROS_WS/site_ws/build/ARS_gazebo_plugin/radar_plugin/catkin_generated/installspace/radar_plugin.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/radar_plugin/cmake" TYPE FILE FILES
    "/home/zonlin/IPP_WorkSpace/ROS_WS/site_ws/build/ARS_gazebo_plugin/radar_plugin/catkin_generated/installspace/radar_pluginConfig.cmake"
    "/home/zonlin/IPP_WorkSpace/ROS_WS/site_ws/build/ARS_gazebo_plugin/radar_plugin/catkin_generated/installspace/radar_pluginConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/radar_plugin" TYPE FILE FILES "/home/zonlin/IPP_WorkSpace/ROS_WS/site_ws/src/ARS_gazebo_plugin/radar_plugin/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/zonlin/IPP_WorkSpace/ROS_WS/site_ws/build/ARS_gazebo_plugin/radar_plugin/catkin_generated/installspace/radar_plugin.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/radar_plugin/cmake" TYPE FILE FILES
    "/home/zonlin/IPP_WorkSpace/ROS_WS/site_ws/build/ARS_gazebo_plugin/radar_plugin/catkin_generated/installspace/radar_pluginConfig.cmake"
    "/home/zonlin/IPP_WorkSpace/ROS_WS/site_ws/build/ARS_gazebo_plugin/radar_plugin/catkin_generated/installspace/radar_pluginConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/radar_plugin" TYPE FILE FILES "/home/zonlin/IPP_WorkSpace/ROS_WS/site_ws/src/ARS_gazebo_plugin/radar_plugin/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/radar_plugin" TYPE DIRECTORY FILES "/home/zonlin/IPP_WorkSpace/ROS_WS/site_ws/src/ARS_gazebo_plugin/radar_plugin/include/radar_plugin/" FILES_MATCHING REGEX "/[^/]*\\.h$" REGEX "/\\.svn$" EXCLUDE)
endif()

