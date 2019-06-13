# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:59:14 2019

@author: DiPu
"""
import requests
url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=4fad345118d926c57b91"
response = requests.get(url)
response.content
jsondata = response.json()
b=int(input("enter no:"))
print("output of conversion from USD to INR is",jsondata["USD_INR"]*b)