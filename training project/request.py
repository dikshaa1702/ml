# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 18:04:11 2019

@author: DiPu
"""

import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'exp':1.8,})
print(r.json())


