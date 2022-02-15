# import everything from tkinter module
from msilib.schema import Font
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
  
# import messagebox from tkinter module
import tkinter.messagebox
from click import style
from numpy import size

from pygame import FULLSCREEN
  
# create a tkinter root window
root = tkinter.Tk()


root.title("Window Popup TEST")
root.geometry('800x800')

  
def buttonOne():
    tkinter.messagebox.showinfo("Left",  "This is the left button.")
def buttonTwo():
    tkinter.messagebox.showinfo("Right",  "This is the Right button.")
def buttonThree():
    tkinter.messagebox.showinfo("Top",  "This is the Top button.")
def buttonFour():
    tkinter.messagebox.showinfo("Bottom",  "This is the Bottom button.")


button1 = Button(root, text="Left", command=buttonOne, height=17, width=37)
button2 = Button(root, text="Right", command=buttonTwo, height=17, width=37)
button3 = Button(root, text="Top", command=buttonThree, height=17, width=37)
button4 = Button(root, text="Bottom", command=buttonFour, height=17, width=37)


button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=TOP)
button4.pack(side=BOTTOM)


root.mainloop()