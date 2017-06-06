from flask import Flask
from flask import request

app = Flask(__name__)

latestImageURL = None

def formatURLImageAsHTML(URL):
    return '<img src="' + latestImageURL + '" alt="Raspberry Pi Image Goes Here!">'

@app.route('/')
def displayImage():

    if latestImageURL == None:
        return "No image has yet been uploaded!"
    else:
        return formatURLImageAsHTML(latestImageURL)

@app.route('/api/updateImage', methods=['POST'])
def updateImageURL():
    data = request.get_json()
    global latestImageURL
    latestImageURL = data['url']
    return 'OK'
