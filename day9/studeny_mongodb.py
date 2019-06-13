# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:19:15 2019

@author: DiPu
"""

import pymongo
client = pymongo.MongoClient("mongodb://dikshaagrawal564:diksha%401702@cluster0-shard-00-00-dswlf.mongodb.net:27017,cluster0-shard-00-01-dswlf.mongodb.net:27017,cluster0-shard-00-02-dswlf.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
mydb=client.diksha
def add_Student(name, age,roll_no, branch):
        mydb.table.insert_one(
            {
            "name" : name,
            "age" : age,
            "roll_no" : roll_no,
            "branch" : branch
            })
        return "Employee added successfully"

def fetch_all_rec():
    user = mydb.table.find()
    for i in user:
        print (i)



add_Student('nEHA',21, 18, 'cs')
add_Student('snEHA',21, 18, 'cs')
fetch_all_rec()
