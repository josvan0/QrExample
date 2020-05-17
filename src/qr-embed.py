#!./venv/python/bin
# -*- coding: utf-8 -*-

import qrcode
from PIL import Image


photo = Image.open('./image.jpg')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L
)

qr.add_data('Content very important :v')
qr.make()
img_qr = qr.make_image()

# calculate position to paste the QR
paste_pos = (photo.size[0] - img_qr.size[0],
             photo.size[1] - img_qr.size[1])

# use method PIL to paste the QR
photo.paste(img_qr, paste_pos)
photo.save('./qr-embed.png')
