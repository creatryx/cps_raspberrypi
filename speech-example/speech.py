import speech_recognition as sr
import requests

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        # Adjust these values as necessary:
        r.pause_threshold = 0.3
        r.non_speaking_duration = 0.3

        # Adjust for noisy environments:
        r.adjust_for_ambient_noise(source)
        print "Now recording, please speak!"

        audio = r.listen(source)

    try:
        # Try to recognize the audio using Google's speech to text:
        text = r.recognize_google(audio, language="en-us", show_all=False)
        # Print out the result:
        print("Speech was: " + text)

        # Recognizing audio directly:
        # baseURL = 'https://api.wit.ai/speech?v=20170409'
        # headers = {'Authorization': 'Bearer 6PPOY2AWDVM5Z6S2GBGHS6RTL264KV76', 'Content-Type': 'audio/wav'}
        # payload = audio.get_wav_data()

        # Recognizing via text:

        # Set the token linked to your wit.ai account:
        headers = {'Authorization': 'Bearer 6PPOY2AWDVM5Z6S2GBGHS6RTL264KV76'}

        # The 'v' parameter here is unique to your application:
        payload = {'v': '20170409', 'q': text}

        resp = requests.get('https://api.wit.ai/message', params=payload, headers=headers)

        # Print out the response from wit.ai; after this you can do what you like with it!
        print resp.url
        print resp.text

    except LookupError:
        # In case of an exception:
        print("Could not translate audio, sorry!")

