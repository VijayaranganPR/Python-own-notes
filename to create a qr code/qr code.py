import pyqrcode
import png
from pyqrcode import QRCode

#The url we want to be in QR

s = ''

#Creating QR Code

url = pyqrcode.create(s)

#Saving file in .svg and .png file

url.svg('QRCODE.svg',scale = 8)
url.png('QRCoDE.png',scale = 5)