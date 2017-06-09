from time import sleep

import requests

import cloudinary
from cloudinary.uploader import upload, destroy

import picamera
camera = picamera.PiCamera()
camera.vflip = True

# You'll need to create a 'credentials.json' file with your Cloudinary credentials stored inside it as JSON.
from credentials import Credentials

cred = Credentials()

cloud_name = cred.retrieveByKey('cloud_name')
api_key = cred.retrieveByKey('api_key')
api_secret = cred.retrieveByKey('api_secret')

config = cloudinary.config(
    cloud_name=cloud_name,
    api_key=api_key,
    api_secret=api_secret
)

def uploadFile(fileName):
    r = upload(fileName)
    try:
        response = upload(fileName)
        return response["url"]
    except Exception as e:
	print("Failed to image file with error: " + str(e))
        return False

while True:

    fileName = 'latest.jpg'

    camera.capture(fileName)

    imageURL = uploadFile(fileName)
    # replace this URL with your PythonAnywhere URL for uploading
    uploadURL = 'http://gzamfirecps.pythonanywhere.com/api/updateImage'

    if imageURL:
        payload = {'url': imageURL}
        result = requests.post(uploadURL, json=payload)
	print("Image upload successful!")
    else:
        print("Image upload failed!")

    sleep(15)
