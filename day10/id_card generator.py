# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:57:43 2019

@author: DiPu
"""
from PIL import Image, ImageDraw, ImageFont
import qrcode
import random

image = Image.new('RGB', (950,900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Roboto-Bold.ttf', size=48)

print('Write Everything in uppercase letters')
(x, y) = (50, 150)
message = "FORSK SUMMER TRAINING PROG"
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('Roboto-Bold.ttf', size=80)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 250)
name=input('\nEnter Your  Name: ')
namef="Name:"+name
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('Roboto-Bold.ttf', size=36)
draw.text((x, y), namef, fill=color, font=font)

(x, y) = (50, 350)
idno=random.randint(1000,5000)
message = str('ID '+str(idno))
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('Roboto-Bold.ttf', size=36)
draw.text((x, y), message, fill=color, font=font)

(x, y) = (50, 550)
college = "College:"+input('\nEnter Your college Name: ')
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('Roboto-Bold.ttf', size=36)
draw.text((x, y), college, fill=color, font=font)

(x, y) = (50, 650)
mob = "College:"+input('\nEnter Your mobile no: ')
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('Roboto-Bold.ttf', size=36)
draw.text((x, y), mob, fill=color, font=font)


(x, y) = (50, 750)
dob = "College:"+input('\nEnter Your Date of birth: ')
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('Roboto-Bold.ttf', size=36)
draw.text((x, y), dob, fill=color, font=font)
# save the edited image 
image.save(str(name)+'.png')
img = qrcode.make(str(idno))   # this info. is added in QR code, also add other things in str function
img.save(str(idno)+'.bmp')


temp = Image.open(name+'.png')       #open saved qr code and save it to final image
im = Image.open(str(idno)+'.bmp')
temp.paste(im,(300,250))
temp.save(name+'.png')


print("id created successfully")
