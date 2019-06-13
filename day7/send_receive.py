# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:22:37 2019

@author: DiPu
"""

import requests
import json
Host = "http://13.127.155.43/api_v0.1/sending"
data = {
        "student":{"Name":"diksha",
        "Phone_No":"7231972592",
        "College_name":"PCE",
        "Branch":"IT"}}

#headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def send():
    response = requests.post(Host,json = data)
    return response

print ( send().text )

    
def get_method():
    response = requests.get("http://13.127.155.43/api_v0.1/receiving")
    return response

print (get_method().text)

