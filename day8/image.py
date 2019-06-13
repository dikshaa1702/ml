# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:49:53 2019

@author: DiPu
"""

import requests
url="http://forsk.in/images/Forsk_logo_bw.png"
source=requests.get(url)
source.content
f=open("my_img.png",'wb')
f.write(source.content)
f.close()


