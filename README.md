# StreamVideO-gstreamer

## Installation

To install GStreamer and necessary plugins, run the following command:

```sh
sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
    libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools \
    gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 \
    gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```

## Streaming Test

To test video streaming using GStreamer, run the following command:

```sh
gnome-terminal -- bash -c "gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! \
    video/x-raw, width=640,height=480,framerate=30/1,format=NV12 ! x264enc bitrate=600 \
    tune=zerolatency ! h264parse ! rtph264pay name=pay0 config-interval=-1 pt=96 ! \
    udpsink host=103.82.249.178 port=8005 sync=false -e; exec bash"
```

This command:
- Captures video from `/dev/video0`
- Converts it to raw video format
- Encodes it using `x264enc` with a bitrate of 600kbps and zero latency tuning
- Parses the H.264 stream and pays it as RTP
- Sends the stream via UDP to the specified host (`103.82.249.178`) on port `8005`
- Runs inside a `gnome-terminal` session

## Setup Server

### Clone Janus-docker-compose

```sh
cd

git clone https://github.com/pondsecret/janus-docker-compose.git

cd janus-docker-compose/

sudo docker compose up
```

### Change Configuration in janus.plugin.streaming.jcfg

```sh
sudo docker exec -it <container id> bash

cd /usr/local/etc/janus/

vim janus.plugin.streaming.jcfg
```

- **Comment all existing configurations**
- **For `rtsp-test`, comment out all RTSP test properties (inside `{}`)**
- **Change `url` to your RTSP link URL and save the file**

```sh
exit

cd janus-docker-compose/
sudo docker compose restart
```

## Notes
- Ensure your system has a working webcam connected at `/dev/video0`
- Modify the `host` and `port` parameters to match your target streaming destination
- You can adjust `width`, `height`, and `bitrate` as needed

### License
This project is open-source. Feel free to modify and use it for your needs.
