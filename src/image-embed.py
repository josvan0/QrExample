#!./venv/python/bin
# -*- coding: utf-8 -*-

import qrcode
from PIL import Image


img = Image.open('./icon.jpg')

qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=2,
    border=5
)

qr.add_data('The image is embed')
qr.make()
img_qr = qr.make_image() # use .convert('RGB') to paste color image

# center QR
pos = ((img_qr.size[0] - img.size[0]) // 2,
       (img_qr.size[1] - img.size[1]) // 2)

img_qr.paste(img, pos)
img_qr.save('./image-embed.png')
