import qrcode
from qrcode.main import QRCode

qr = qrcode.QRCode(

    version= 1,
    box_size= 15,
    border = 15
)

link = "http://subhasreesahoo.com/#"

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill = 'black',back_color = 'white')
img.save("weblink.png")






