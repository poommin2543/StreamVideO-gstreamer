#!/bin/bash

#gnome-terminal --tab --title="tab 1" --command="source ~Documents/ublox_ws/devel/setup.sh; roslaunch ublox_gps ublox_zed-f9p.launch; $SHELL'" 
#gnome-terminal -- bash -c "source ~/Documents/ublox_ws/devel/setup.sh; roslaunch ublox_gps ublox_zed-f9p.launch; exec bash"
#sleep 15

#gnome-terminal --tab --title="tab 1" --command="source Documents/info_gps_ws/devel/setup.sh; rosrun info_gps Info_NavSatFix.py; $SHELL'" 
#gnome-terminal -- bash -c "source Documents/info_gps_ws/devel/setup.sh; rosrun info_gps Info_NavSatFix.py; exec bash"

#sleep 3
#gnome-terminal --tab --title="tab 1" --command="gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! video/x-raw, width=640,height=480,framerate=30/1,format=NV12 ! x264enc bitrate=600 tune=zerolatency ! h264parse ! rtph264pay name=pay0 config-interval=-1 pt=96 ! udpsink host=34.143.225.243 port=8004 sync=false -e; $SHELL'" 

#gnome-terminal -- bash -c "htop"

#gnome-terminal -- bash -c "gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! video/x-raw, width=640,height=480,framerate=30/1,format=NV12 ! x264enc bitrate=600 tune=zerolatency ! h264parse ! rtph264pay name=pay0 config-interval=-1 pt=96 ! udpsink host=34.143.225.243 port=8004 sync=false -e; exec bash"

#gnome-terminal -- bash -c "gst-launch-1.0 v4l2src device=/dev/video1 ! videoconvert ! video/x-raw, width=640,height=480,framerate=30/1,format=NV12 ! x264enc bitrate=600 tune=zerolatency ! h264parse ! rtph264pay name=pay0 config-interval=-1 pt=96 ! udpsink host=34.143.225.243 port=8005 sync=false -e; exec bash"

#gnome-terminal -- bash -c "gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! video/x-raw, width=640,height=480,framerate=30/1,format=NV12 ! x264enc bitrate=600 tune=zerolatency ! h264parse ! rtph264pay name=pay0 config-interval=-1 pt=96 ! udpsink host=103.82.249.178 port=8004 sync=false -e; exec bash"

gnome-terminal -- bash -c "python cameraopen/multicam.py; exec bash"

#gnome-terminal -- bash -c "gst-launch-1.0 v4l2src device=/dev/video3 ! videoconvert ! video/x-raw, width=640,height=480,framerate=30/1,format=NV12 ! x264enc bitrate=600 tune=zerolatency ! h264parse ! rtph264pay name=pay0 config-interval=-1 pt=96 ! udpsink host=34.143.225.243 port=8005 sync=false -e; exec bash"

node '/home/jetson/Documents/mqttjs/app.js'
