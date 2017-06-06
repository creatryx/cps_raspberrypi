# Begin by installing the camera module to get access to the Pi's onboard camera:

# sudo apt-get update

# sudo apt-get install python3-picamera
# OR
# sudo apt-get install python-picamera

# We'll also have to install Cloudinary. We'll use Cloudinary as the host for our images.

# sudo apt-get install cloudinary

from time import sleep

import requests

import cloudinary
from cloudinary.uploader import upload, destroy

import picamera
camera = picamera.PiCamera()

config = cloudinary.config(
    cloud_name='ds1fs8ef4',
    api_key='794785675884621',
    api_secret='GPZz7t9rp0eaTUceJFA36lGcn9M'
)

def uploadFile(fileName):
    try:
        response = upload(fileName)
        return response["url"]
    except:
        return False

while True:

    fileName = 'latest.jpg'

    camera.capture(fileName)

    imageURL = uploadFile(fileName)

    uploadURL = 'http://gzamfirecps.pythonanywhere.com/api/updateImage'

    if imageURL:
        payload = {'url': imageURL}
        result = requests.post(uploadURL, json=payload)
    else:
        print("File upload failed!")

    sleep(15)
