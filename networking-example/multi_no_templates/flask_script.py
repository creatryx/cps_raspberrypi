from flask import Flask
from flask import request

app = Flask(__name__)

latestImageURL = None
displayImages = []
maxToDisplay = 100

# True: images will cycle, like a GIF
# False: images will display sequentially
scriptsEnabled = True

def getScript(file=None, url=None):
    '''
    Retrieves and returns the stringified version of the specified script file.

    Keyword arguments:
    file -- the file name, passed in as a string (default None)
    url -- the URL where the script can be found, passed in a string (default None)
    '''
    if file is not None:
        try:
            return "<script>" + open(file, 'r').read() + "</script>"
        except:
            raise ValueError("Unable to read the specified script file.")
    if url is not None:
        return '<script src="' + url + '"></script>'

    raise ValueError("Invalid script specifier.")

def getAllScripts():
    if scriptsEnabled:
        js = getScript(url="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js")
        js += getScript(file="imageMagic.js")
        return js
    else:
        return ''

def getImages():
    imagesCount = str(len(displayImages))

    # Top counter div; displays image count to user and serves as indicator to script.
    htmlString = '<div id="counter" count="' + imagesCount + '">' + imagesCount + ' images to display! </div><br>'

    # Main image div; images will cycle into here.
    htmlString += "<img id='current' style='transform: rotate(90deg)' src='' alt='Images should appear here...'><br>"

    # Loop through the images in the queue, starting at the tail end and decrementing by 1.
    for imageNumber in range(len(displayImages) - 1, -1, -1):
        currentImage = displayImages[imageNumber]
        htmlString += '<img id="' + str(imageNumber) + '" role="preload" src="' + currentImage + '" alt="Raspberry Pi Image Goes Here!"><br>'

    return htmlString

def addImageToQueue(URL):
    if len(displayImages) == maxToDisplay:
        displayImages.pop(0)
    displayImages.append(URL)

@app.route('/')
def displayPage():
    return getAllScripts() + getImages()

@app.route('/api/updateImage', methods=['POST'])
def updateImageURL():
    data = request.get_json()
    # global latestImageURL
    latestImageURL = data['url']
    addImageToQueue(latestImageURL)
    return 'OK'
