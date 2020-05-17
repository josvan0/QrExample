#!./venv/bin/python
# -*- coding: utf-8 -*-

import qrcode


# create QR with some settings
# version and error_correction accorfing to QR standards
# box_size -> pixel size of squares
# border -> padding image (n * box_size(px))
qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=2,
    border=8
)

# set data and make the QR
qr.add_data('QR created by object')
qr.make()

# create image, accept basic colors words or HEX
img = qr.make_image(fill_color='black', back_color='#ffffff')
img.save('./object.png')
