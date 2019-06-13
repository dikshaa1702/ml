# -*- coding: utf-8 -*-
"""
Created on Fri May 10 19:38:23 2019

@author: DiPu
"""
 
users = {} 
with open('passwd.txt') as f:
    for line in f:
        if not line.startswith("#"):
            user_info = line.split(":")
            users[user_info[0]] = user_info[2]
 
for username in sorted(users):
    print("{}:{}".format(username, users[username]))
 
