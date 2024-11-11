import tkinter
from tkinter.ttk import *
from tkinter import filedialog as fd 
from PIL import ImageTk, Image
import os
import text_lang_convert
from gtts import gTTS
import os
from googletrans import Translator
import  vlc
import time
import cv2
import obj_detection
def ocr_load():
    print("Loaded OCR")
    print("Opening Camera")
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0
    print("opened")
    while True:
        #print("reading cam")
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "Clicked_image.jpg"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            break
    cam.release()
    cv2.destroyAllWindows()
    text_lang_convert.genrate()
    
def obj_load():
    obj_detection.object_detect()
    def playhindi():
        p=vlc.MediaPlayer('speech_hindi_o.mp3')
        p.play()
    def playkannada():
        p=vlc.MediaPlayer('speech_kannada_o.mp3')
        p.play()
    def playtelugu():
        p=vlc.MediaPlayer('speech_telugu_o.mp3')
        p.play()
    def playtamil():
        p=vlc.MediaPlayer('speech_tamil_o.mp3')
        p.play()
    def playmarathi():
        p=vlc.MediaPlayer('speech_marathi_o.mp3')
        p.play()
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
    btn1.grid(row=4, column=0, padx=10)
    ocr_w.mainloop()
    
master=tkinter.Tk()
master.title("Text to speech")
master.geometry("450x350")

button1=tkinter.Button(master, text="OCR", command=ocr_load)
button1.pack(side=tkinter.LEFT)

button2=tkinter.Button(master, text="Detect Object", command=obj_load)
button2.pack(side=tkinter.RIGHT)


master.mainloop()
