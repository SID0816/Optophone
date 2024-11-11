import requests
import json
import base64
from gtts import gTTS
import os
import time
from googletrans import Translator
import  vlc
import tkinter as tk
def genrate():
    def destroy_widgets():
        option_label.destroy()
        option_menu.destroy()
        button.destroy()

    def create_new_button(lang,text):
        def another_function():
            myobj = gTTS(text=text, lang=lang, slow=False)
            myobj.save("speech_english_k.mp3")
            p=vlc.MediaPlayer('speech_english_k.mp3')
            p.play()
            time.sleep(10)
        new_button = tk.Button(root, text="Play sound", command=another_function)
        new_button.place(x=50, y=100)
    def button_click(opt):
        if opt=='Kannada':
            lang='kn'
        elif opt=='Hindi':
            lang='hi'
        else:
            lang='en'
        destroy_widgets()
        text=gen_text()
        create_new_button(lang,text)
        
    def gen_text():
        api_key = "AIzaSyBc7M_1QB7hUNi3Ho8-sGbmi0TVXvDoaRA"
        url = "https://vision.googleapis.com/v1/images:annotate?key=" + api_key
        answer=''
        file_path = "./Clicked_image.jpg"
        with open(file_path,'rb') as image_file:
            image_content = image_file.read()
        image_content_base64 = base64.b64encode(image_content).decode('utf-8')
        request_json = {
          "requests": [
            {
              "image": {
                "content": image_content_base64
              },
              "features": [
                {
                  "type": "DOCUMENT_TEXT_DETECTION"
                }
              ]
            }
          ]
        }

        # Send the request to the Vision API
        response = requests.post(url, data=json.dumps(request_json))

        # Process the response
        response_json = json.loads(response.text)

        if 'error' in response_json:
            print(f"Error: {response_json['error']['message']}")
        elif 'responses' in response_json and response_json['responses'][0].get('fullTextAnnotation'):
            text = response_json['responses'][0]['fullTextAnnotation']['text']
            answer+=text
        else:
            print(f"No text found in image {name}")
        answer=answer.replace('\n', ' ')
        answer=answer.replace('\t', ' ')
        return answer

    root = tk.Tk()
    root.geometry("200x150")

    # Label for Option Menu
    option_label = tk.Label(root, text="Select an option:")
    option_label.place(x=50, y=20)

    # Option Menu
    options = ["Kannada", "Hindi", "English"]
    selected_option = tk.StringVar(root)
    selected_option.set(options[0])
    option_menu = tk.OptionMenu(root, selected_option, *options)
    option_menu.place(x=50, y=50)

    # Button
    button = tk.Button(root, text="Convert", command=lambda: button_click(selected_option.get()))
    button.place(x=50, y=80)

    root.mainloop()

