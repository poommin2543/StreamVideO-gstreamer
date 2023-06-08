"# StreamVideO-gstreamer" 
// install Gstreamer-launch 1.0 

sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

//test
#gnome-terminal -- bash -c "gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! video/x-raw, width=640,height=480,framerate=30/1,format=NV12 ! x264enc bitrate=600 tune=zerolatency ! h264parse ! rtph264pay name=pay0 config-interval=-1 pt=96 ! udpsink host=103.82.249.178 port=8005 sync=false -e; exec bash"
