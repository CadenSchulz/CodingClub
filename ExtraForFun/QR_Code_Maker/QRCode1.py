# ----> Step 1: type "pip install qrcode[pil]" in terminal

# ----> Step 2: import qrcode API
import qrcode

# ----> Step 3: Define variable/input user message
img = qrcode.make(input('Your Message: '))

# ----> Step 4: Create path to send generated QR Code to
img.save("H:/.shortcut-targets-by-id/1qVslRslzOPZF6I_um-7kptss53kZwZVP/Schulz, Caden/ExtraForFun/QR_Code_Maker/QRCode1.jpg")