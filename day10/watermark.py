# -*- coding: utf-8 -*-
"""
Created on Sun May 19 15:36:28 2019

@author: DiPu
"""

from PIL import Image

def image_watermark(image):
    temp1=Image.open(image)
    #adding logo
    im=Image.open('dk.png')
    temp1.paste(im,(280,600))
    temp1.save(image)
image_watermark('temp.jpg')