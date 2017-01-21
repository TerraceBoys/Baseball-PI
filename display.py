# !/usr/bin/python

# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

import time
import traceback

import Image
import ImageDraw
import ImageFont
from rgbmatrix import Adafruit_RGBmatrix

matrix = Adafruit_RGBmatrix(32, 2)
text_font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf", 8)
num_font = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSans.ttf", 11)



def main():
    image = Image.new("RGB", (64, 32))  # Can be larger than matrix iff wanted!!
    draw = ImageDraw.Draw(image)  # Declare Draw instance before prims
    draw.text((2, 1), "Baseball", font=text_font, fill="white")
    draw.line((0, 0, 63, 0), fill="#400080")
    draw.text((4, 10), train1, font=num_font, fill="orange")
    matrix.Clear()
    matrix.SetImage(image.im.id, 0, 0)
