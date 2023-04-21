import cv2
import numpy as np

gst_str_rtp = " appsrc ! videoconvert ! videoscale ! video/x-raw,format=I420,framerate=52/1 !  videoconvert ! \
     x264enc tune=zerolatency bitrate=1200 speed-preset=superfast ! rtph264pay ! udpsink host=103.82.249.178 port=8005"   
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter(gst_str_rtp, fourcc, 52, (1280, 240), True)

img = cv2.imread("//home//jetson//cameraopen//img.png", cv2.IMREAD_COLOR)
resized_img = cv2.resize(img, (320, 240), interpolation=cv2.INTER_LINEAR)
images = np.hstack((resized_img, resized_img, resized_img, resized_img))

while True:
    try:
        # cv2.imshow('img1', images)
        out.write(images)
        # print("Writing")
    except Exception:
        print("Error writing")

    # print('writing frame')
    if cv2.waitKey(1) == ord('q'):
        break
    


# Release everything if job is finished
img.release()
# cap1.release()
# cap2.release()
# cap3.release()
# ipcap.release()
out.release()