from tkinter import *
from tkinter import filedialog as fd 
from PIL import ImageTk, Image
import os

def openfile():
   filepath= fd.askopenfilename()
   onlyfilename = os.path.basename(filepath)
   mylabel.config(text=onlyfilename)

myscreen=Tk()
filebutton=Button(text='choose your file',command=openfile)
filebutton.grid(row=0,column=2)
mylabel = Label(myscreen, text="You chossen file path will be displayed here")
mylabel.grid(row=1,column=2)
myscreen.mainloop()