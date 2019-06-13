# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:25:03 2019

@author: DiPu
"""
import requests
id1="http://api.openweathermap.org/data/2.5/weather?q=Jaipur"
id2="&appid=68e15f12e7d616e93233953140cec347"
id=id1+id2
response = requests.get(id)
b=response.content
jsondata=response.json()
print("coordinates:",jsondata["coord"])
print("sunrise:",jsondata["sunrise"])
print("sunset:",jsondata["sunset"])
print("weather condition:",jsondata["main"])
