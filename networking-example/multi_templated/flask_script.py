from flask import Flask, render_template
from flask import request

app = Flask(__name__)

latestImageURL = None
displayImages = []
maxToDisplay = 100

def addImageToQueue(URL):
    if len(displayImages) == maxToDisplay:
        displayImages.pop(0)
    displayImages.append(URL)

@app.route('/api/updateImage', methods=['POST'])
def updateImageURL():
    data = request.get_json()
    # global latestImageURL
    latestImageURL = data['url']
    addImageToQueue(latestImageURL)
    return 'OK'

@app.route('/')
def displayPage():

    # reverse the displayImages list for easier processing
    orderedImages = displayImages[::-1]

    # tag each image with a number indicating its position
    numberedImages = zip(orderedImages, range(len(orderedImages)))

    # map the above onto a standard object structure
    imageObjects = map(lambda imageData : {'url': imageData[0], 'count': imageData[1]}, numberedImages)

    return render_template('main.html',
                            imagesCount = len(displayImages),
                            imageObjects = imageObjects)
