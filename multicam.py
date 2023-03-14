import cv2
import numpy as np
# print(cv2.getBuildInformation())
# ipcap = cv2.VideoCapture("rtsp://lordtopzz01:Siripong01@192.168.50.59:554/stream1")
# ipcap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# ipcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 15)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap1 = cv2.VideoCapture(1)
cap1.set(cv2.CAP_PROP_FPS, 15)
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap2 = cv2.VideoCapture(2)
cap2.set(cv2.CAP_PROP_FPS, 15)
cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap3 = cv2.VideoCapture(3)
cap3.set(cv2.CAP_PROP_FPS, 15)
cap3.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap3.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
# out = cv2.VideoWriter("appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=BGRx ! nvvidconv ! omxh264enc ! video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host=10.168.1.177 port=50001", cv2.CAP_GSTREAMER, 0, 25.0, (1920,1080))
# out = cv2.VideoWriter("appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=BGRx ! nvvidconv ! omxh264enc ! video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host=103.82.249.178 port=8005", cv2.CAP_GSTREAMER, 0, 25.0, (640,480))
# out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=1500 ! rtph264pay ! udpsink host=103.82.249.178 port=8005',cv2.CAP_GSTREAMER,0, 25, (640,480), True)
# out = cv2.VideoWriter("appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=BGRx ! nvvidconv ! omxh264enc ! video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host=10.168.1.177 port=50001", cv2.CAP_GSTREAMER, 0, 25.0, (1920,1080))
# gst_str_rtp = "appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! udpsink host=103.82.249.178 port=8004"
# out = cv2.VideoWriter(gst_str_rtp, 0, 30, (640, 480), True)
# gst_str_rtp = "appsrc ! video/x-raw,format=BGR ! queue ! videoconvert ! video/x-raw,format=BGRx ! nvvidconv !\
#      video/x-raw(memory:NVMM),format=NV12,width=640,height=360,framerate=52/1 ! nvv4l2h264enc insert-sps-pps=1  \
#         insert-vui=1 idrinterval=30bitrate=1000000 EnableTwopassCBR=1  ! h264parse ! rtph264pay ! udpsink host=103.82.249.178 port=8005 auto-multicast=0"
# gst_str_rtp = " appsrc ! videoconvert ! videoscale ! video/x-raw,format=I420,framerate=52/1 !  videoconvert !\
#      x264enc tune=zerolatency bitrate=600 speed-preset=superfast ! rtph264pay ! udpsink host=103.82.249.178 port=8005" 
gst_str_rtp = " appsrc ! videoconvert ! videoscale ! video/x-raw,format=I420,framerate=52/1 !  videoconvert ! \
     x264enc tune=zerolatency bitrate=600 speed-preset=superfast ! rtph264pay ! udpsink host=103.82.249.178 port=8005"   
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter(gst_str_rtp, fourcc, 52, (1280, 240), True)
# out = cv2.VideoWriter(gst_str_rtp, cv2.CAP_GSTREAMER, 0, float(52), (640, 480), True)

while cap.isOpened():
    ret, frame = cap.read()
    # assert ret
    ret1, frame1 = cap1.read()
    # assert ret1
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    # assert ret2cc
    # ret2, frame2 = ipcap.read()
    # assert ret2
    # resized = cv2.resize(frame, (640,360), interpolation = cv2.INTER_AREA)
    if ret:
        try:
            images = np.hstack((frame, frame1,frame2,frame3))
            # cv2.imshow('img1',images)
            out.write(images)
            # print("Writing")
            # print(out)
        except Exception:
            print("Error writing")
        # print('writing frame')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    


# Release everything if job is finished
cap.release()
cap1.release()
cap2.release()
cap3.release()
# ipcap.release()
out.release()