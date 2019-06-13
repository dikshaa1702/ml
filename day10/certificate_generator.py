# -*- coding: utf-8 -*-
"""
Created on Fri May 17 12:33:19 2019

@author: DiPu
"""
#for border import ImageOps for creating image import ImageDraw for fon addition use ImageFont
from PIL import Image  ,ImageDraw ,ImageFont ,ImageOps 
image=Image.new('RGB',(1024,761),color=(244,247,245))
draw=ImageDraw.Draw(image)
image.save('certificate.png')
#adding border to the certificate


# adding text to image

font = ImageFont.truetype("Roboto-Italic.ttf",48)
(x, y) = (50,50)
message = "FORSK TECHNOLOGIES PRIVATE LIMITED"
color = 'rgb(60,76,102)' # black color
draw.text((x,y),message,fill=color,font=font)
image.save('certificate.png')

font = ImageFont.truetype("Roboto-BoldItalic.ttf",48)
(x, y) = (250,300)
message1 = "TRAINING CERTIFICATE"
color = 'rgb(68,131,135)' # black color
draw.text((x,y),message1,fill=color,font=font)
image.save('certificate.png')

color='rgb(0,0,0)'
font = ImageFont.truetype("Roboto-Medium.ttf",36)
(x, y) = (50,400)
message = str(
"This is to certify that Mr./Ms./ " +input("enter name:")+  '   '  +  "student of " +'   '+input("enter your college name:")+'   '
+   "\n Branch "   +' '  +  input("enter Branch:") + '   ' +  "has completed successfully summer/training in "
+"\n Machine learning for the period from "+'   '+ input("enter start date:")+'   '+"to"+'   '
+ "\n"+input("enter end date:")+"."
+ '\n  ' +   "Duration"     +'  ' +input("enter no of weeks:")+"   "+  "weeks/months."
)

draw.multiline_text((x,y),message,fill=color,font=font)
image.save('certificate.png')


#ADDING LOGO
temp=Image.open('certificate.png')
im=Image.open('data.jpg')
temp.paste(im,(520,150))
temp.save('certificate.png')

#ADDING SEAL
temp1=Image.open('certificate.png')
im=Image.open('logo.jpg')
temp1.paste(im,(900,650))
temp1.save('certificate.png')

3#ADDING SIGNATURE
temp2=Image.open('certificate.png')
im=Image.open('signf.png')
temp2.paste(im,(280,600))
temp2.save('certificate.png')


font = ImageFont.truetype("Roboto-BoldItalic.ttf",36)
(x, y) = (50,700)
message4 = "Signed by"
color = 'rgb(68,131,135)' # black color
draw.text((x,y),message4,fill=color,font=font)
image.save('certificate.png')

#image=ImageOps.expand(image,border=50,fill='rgb(28,25,26)')
#image.save('certificate.png')

print("CERTIFICATE HAS BEEN CREATED")





