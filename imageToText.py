import tkinter
from tkinter.ttk import *
from tkinter import filedialog as fd 
from PIL import ImageTk, Image
import pytesseract
import re
from gtts import gTTS
import os
from googletrans import Translator
import  vlc
import time
import speech_recognition as sr
def ocr_code(file_path):
    from PIL import Image
    import pytesseract
    import re
    from gtts import gTTS
    import os
    from googletrans import Translator
    import  vlc
    import time
    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = Image.open(file_path)
    text = pytesseract.image_to_string(img)
    #print(text.strip())
    text1=''
    translator=Translator()
    for k in text.split("\n"):
        if k=='\n':
            text1+=' '
            continue
        s=re.sub(r"[^a-zA-Z0-9]+", ' ', k)
        text1=text1+s
    print(text1)
    """mytext = text1
               
    language = 'en'
              
    myobj = gTTS(text=mytext, lang=language, slow=False) 
               
    myobj.save("speech_english_t.mp3") 

    #retrieve mp3 file 
    

    filename='./speech_english_t.mp3'
    os.system("mpg321 speech_english_t.mp3")
    p=vlc.MediaPlayer('speech_english_t.mp3')
    p.play()

    attachment =open(filename,'rb')"""

    
    test_to_translate_english=translator.translate(text1,src='en',dest='en')
    test_to_translate_hindi=translator.translate(text1,src='en',dest='hi')
    test_to_translate_kannada=translator.translate(text1,src='en',dest='kn')
    test_to_translate_telugu=translator.translate(text1,src='en',dest='te')
    test_to_translate_tamil=translator.translate(text1,src='en',dest='ta')
    test_to_translate_marathi=translator.translate(text1,src='en',dest='mr')
    obj_english=gTTS(text=test_to_translate_english.text,lang='en',slow=False)
    obj_english.save("speech_english_t.mp3")
    obj_hindi=gTTS(text=test_to_translate_hindi.text,lang='hi',slow=False)
    obj_hindi.save("speech_hindi_t.mp3")
    obj_kannada=gTTS(text=test_to_translate_kannada.text,lang='kn',slow=False)
    obj_kannada.save("speech_kannada_t.mp3")
    obj_telugu=gTTS(text=test_to_translate_telugu.text,lang='te',slow=False)
    obj_telugu.save("speech_telugu_t.mp3")
    obj_tamil=gTTS(text=test_to_translate_tamil.text,lang='ta',slow=False)
    obj_tamil.save("speech_tamil_t.mp3")
    obj_marathi=gTTS(text=test_to_translate_marathi.text,lang='mr',slow=False)
    obj_marathi.save("speech_marathi_t.mp3")
    playsoundsText()
def playsoundsText():
    def playhindi():
        p=vlc.MediaPlayer('speech_hindi_t.mp3')
        p.play()
    def playkannada():
        p=vlc.MediaPlayer('speech_kannada_t.mp3')
        p.play()
    def playtelugu():
        p=vlc.MediaPlayer('speech_telugu_t.mp3')
        p.play()
    def playtamil():
        p=vlc.MediaPlayer('speech_tamil_t.mp3')
        p.play()
    def playmarathi():
        p=vlc.MediaPlayer('speech_marathi_t.mp3')
        p.play()
    def playenglish():
        p=vlc.MediaPlayer('speech_english_t.mp3')
        p.play()
    '''
    ocr_w=tkinter.Tk()
    ocr_w.title("Text to Speech")
    ocr_w.geometry("450x350")
    btn1 = Button(
    ocr_w, 
    text ='Play Kannada', 
    command = playkannada
    )
    btn1.grid(row=0, column=0, padx=10)
    btn2 = Button(
    ocr_w, 
    text ='Play Hindi', 
    command = playhindi
    )
    btn2.grid(row=1, column=0, padx=10)
    btn3 = Button(
    ocr_w, 
    text ='Play Telugu', 
    command = playtelugu
    )
    btn3.grid(row=2, column=0, padx=10)
    btn4 = Button(
    ocr_w, 
    text ='Play Tamil', 
    command = playtamil
    )
    btn4.grid(row=3, column=0, padx=10)
    btn5 = Button(
    ocr_w, 
    text ='Play Marathi', 
    command = playmarathi
    )
    btn5.grid(row=4, column=0, padx=10)
    btn6 = Button(
    ocr_w, 
    text ='Play English', 
    command = playenglish
    )
    btn6.grid(row=4, column=0, padx=10)
    ocr_w.mainloop()
    '''
    while True:    
        try:
            rr = sr.Recognizer()
            with sr.Microphone() as source3:
                rr.adjust_for_ambient_noise(source3, duration=0.2)
                
                
                
                print("Say something:")
                #listens for the user's input
                audio2 = rr.listen(source3)
                # Using google to recognize audio
                myspeech_is = rr.recognize_google(audio2)
                print(myspeech_is)
                if myspeech_is=='Kannada':
                    playkannada()
                if myspeech_is=='Hindi':
                    playhindi()
                if myspeech_is=='Telugu':
                    playtelugu()
                if myspeech_is=='Tamil':
                    playtamil()
                if myspeech_is=='Marathi':
                    playmarathi()
                if myspeech_is=='English':
                    playenglish()
                #return myspeech_is
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            t
            
            
        except sr.UnknownValueError:
            print("unknown error occurred")
            
