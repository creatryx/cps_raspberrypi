from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import numpy as np
import cv2

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 2
rawCapture = PiRGBArray(camera, size=(640, 480))

face_cascade = cv2.CascadeClassifier('/home/jd/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

time.sleep(0.1)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = cv2.flip(frame.array, -1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)    
    
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)
    if key == ord("q"):
        break
