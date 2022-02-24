# ----> Step 1a: Imports
from ctypes import resize
from msilib.schema import TextStyle
from tkinter import font
from turtle import width
from click import style
from matplotlib.pyplot import text
import pyqrcode
from PIL import ImageTk, Image  
    # ----> Step 1b: define URL Variable (Path)
url = pyqrcode.create('https://caden/')
print(url.terminal(quiet_zone=1))

from tkinter import *
from tkinter import messagebox
import pyqrcode

# ----> Step 2: Define Variables
ws = Tk()
ws.title("QR Code Generator")
ws.config(bg='#F25252')

# ----> Step 3: Create Heading/Image at Bottom
Label(ws, text = 'Benet Academy', font =('Comic Sans MS', 12, font.BOLD)).pack(side = TOP, padx = 50)

'''
photo = PhotoImage(file = "H:/.shortcut-targets-by-id/1qVslRslzOPZF6I_um-7kptss53kZwZVP/Schulz, Caden/ExtraForFun/Pictures/redwing.jpg")
photoimage = photo.subsample(3, 3)
Button(ws, image = photoimage, width = 250, height= 250).pack(side = BOTTOM, pady = 5)
'''

# ----> Step 3: Require all fields/Warning Message
def generate_QR():
    if len(user_message.get())!=0 :
        global qr,img
        qr = pyqrcode.create(user_message.get())
        img = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showwarning('Warning', 'Please enter a message or URL!')
    try:
        display_code()
    except:
        pass

# ----> Step 4: Below Generated QR Code/Preview of message/URL
def display_code():
    label2.config(image = img)
    final_product.config(text='QR Code Generated!', font= ('Comic Sans MS', '12', 'bold'),)
                            # "QR code of " + user_message.get()

# ----> Step 5: Label Title
label1 = Label(
    ws,
    text="Enter message or URL",
    font= ('Comic Sans MS', '20', 'bold'),
    height=5,
    width=25,
    bg='#F25252'
    )
label1.pack()

# ----> Step 6: Input message/url from user
user_message = StringVar()
message = Entry(
    ws,
    font= ('Comic Sans MS', '15', 'bold'),
    textvariable = user_message,
    width= 50,
    )
message.pack(padx=50)

# ----> Step 7: Generate QR Code Button
generate = Button(
    ws,
    text = "Generate QR Code",
    width=15,
    height=3,
    font= ('Comic Sans MS', '15', 'bold'),
    command = generate_QR
    )
generate.pack(pady=40)

# ----> Step 8: Output/QR Code Generated
label2 = Label(
    ws,
    bg='#F25252')
label2.pack()
final_product = Label(
    ws,
    text="Go Redwings!",
    font= ('Comic Sans MS', '12', 'bold'),
    bg='#F25252'
    )
final_product.pack()

ws.mainloop()