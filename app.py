from flask import Flask, render_template
import gtts
import os
from playsound import playsound

app = Flask(__name__)

@app.route('/')
def index():
    text = "Hii,  I am arpan.  It's my new project for text to speach convertor.  You can use easily."
    sound = gtts.gTTS(text, lang='en')
    sound.save("static/welcome.mp3")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
