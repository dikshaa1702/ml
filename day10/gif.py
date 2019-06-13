# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:10:17 2019

@author: DiPu
"""
#imageio is used for making video clips either short or long
import imageio
filenames = ['gif1.jpg','gif2.jpg','gif3.jpg','gif4.jpg']
images=[]
for im in filenames:
    images.append(imageio.imread(im))
duration=1
imageio.mimsave('birds.gif', images,duration)