#!./venv/python/bin
# -*- coding: utf-8 -*-

import qrcode


img = qrcode.make('Hello world!')  # create a PilImage

print(type(img))  # can use this object like Pillow(PIL)
# size[0] = x | size[1] = y
print(f'Dims: {img.size[0]}x{img.size[1]} px')

# creates the image file
img.save('./hello.png')
