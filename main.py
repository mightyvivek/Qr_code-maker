import pyqrcode
import png
from pyqrcode import QRCode

s = "https://github.com/mightyvivek"
#img = Vivek.jpeg 

url = pyqrcode.create(s, mode='binary')
#url.svg("myqr.svg", scale = 8)
url.png('myqr2.png', scale = 6)
url.show()

