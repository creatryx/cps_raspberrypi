### Networking Example

Begin by installing the camera module to get access to the Pi's onboard camera:

```
sudo apt-get update

sudo apt-get install python-picamera
sudo apt-get install python3-picamera # for python3
```

You should also install Cloudinary. This code uses Cloudinary as the host for images.

```
pip install cloudinary
pip3 install cloudinary # for python3
```

You'll need an account at Cloudinary; once you have that account, copy `credentials-sample.json` into a new file called `credentials.json` and update the three lines there with your Cloudinary credentials.