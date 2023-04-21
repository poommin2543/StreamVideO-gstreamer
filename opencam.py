import cv2
import numpy as np
""" 
gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
Flip the image by setting the flip_method (most common values: 0 and 2)
display_width and display_height determine the size of each camera pane in the window on the screen
Default 1920x1080 displayd in a 1/4 size window
"""

def gstreamer_pipeline(
    sensor_id=1,
    capture_width=640,
    capture_height=480,
    display_width=640,
    display_height=480,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d !"
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


def show_camera():
    window_title = "CSI Camera"
    gst_str_rtp = "appsrc ! videoconvert ! x264enc noise-reduction=10000 tune=zerolatency byte-stream=true threads=4 " \
              " ! h264parse ! mpegtsmux ! rtpmp2tpay ! udpsink host=34.143.225.243 port=8005"
    # To flip the image, modify the flip_method parameter (0 and 2 are the most common)
    # print(gstreamer_pipeline(sensor_id=1,flip_method=0))
    # video_capture1 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=1,flip_method=0), cv2.CAP_GSTREAMER)
    # print(gstreamer_pipeline(sensor_id=0,flip_method=0))
    # video_capture0 = cv2.VideoCapture(gstreamer_pipeline(sensor_id=0,flip_method=0), cv2.CAP_GSTREAMER)
    video_capture0 = cv2.VideoCapture(2)
    # out = cv2.VideoWriter("appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=BGRx ! nvvidconv ! omxh264enc ! video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host=34.143.225.243 port=8004", cv2.CAP_GSTREAMER, 0, 25.0, (1280,480))
    # out = cv2.VideoWriter(gst_str_rtp, cv2.CAP_GSTREAMER, 0, 25.0, (1280,480))
    out = cv2.VideoWriter(gst_str_rtp, 0, 25, (1280, 480), True)
    if video_capture0.isOpened():
        try:
            
            window_handle = cv2.namedWindow(window_title, cv2.WINDOW_AUTOSIZE)
            while True:
                ret_val0, frame0 = video_capture0.read()
                # ret_val1, frame1 = video_capture1.read()
                
                # ret_val2, frame2 = video_capture2.read()
                # combined_frame = np.concatenate((frame0, frame1), axis=1)
                # combined_frame = np.concatenate((frame0, frame1,cv2.resize(frame2, (640, 480))), axis=1)
                # Check to see if the user closed the window
                # Under GTK+ (Jetson Default), WND_PROP_VISIBLE does not work correctly. Under Qt it does
                # GTK - Substitute WND_PROP_AUTOSIZE to detect if window has been closed by user
                if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                    # cv2.imshow(window_title, combined_frame)
                    out.write(frame0)
                    cv2.imshow(window_title+"1", frame0)
                else:
                    break 
                keyCode = cv2.waitKey(10) & 0xFF
                # Stop the program on the ESC key or 'q'
                if keyCode == 27 or keyCode == ord('q'):
                    break
        finally:
            video_capture0.release()
            # video_capture1.release()
            out.release()
            cv2.destroyAllWindows()
    else:
        print("Error: Unable to open camera")


if __name__ == "__main__":
    show_camera()