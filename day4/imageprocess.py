# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:05:57 2019

@author: DiPu
"""

from PIL import Image
ip=input("enter image name:")
img=Image.open(ip).convert('L')
img.show()

img_rotate = img.rotate(90)
img_rotate.show() 

width,height=img_rotate.size
hw=width/2
hh=height/2

img_rotate=img_rotate.crop((hw-80,hh-102,hw+80,hw+102))
img.show()

img_rotate.thumbnail((75,75))
img_rotate.show()
 