from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import numpy as np
import cv2

camera = PiCamera()
camera.resolution = (160,120)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(160, 120))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
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
