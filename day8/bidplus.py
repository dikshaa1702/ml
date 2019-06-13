# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:12:50 2019

@author: DiPu
"""
import pandas as pd
from selenium import webdriver
driver = webdriver.Chrome(r"G:\ml training\chromedriver")
url = "https://bidplus.gem.gov.in/bidlists"
driver.get(url)


conn = mysql.connector.connect ( user='root', password='', host='localhost')

c=conn.cursor()

A=[]
BID_NO=[]
items=[]
Quantity_Required=[]
Department_Name_address =[] 
Start_date=[]
Start_time=[]
End_date=[]
b=[]
Start_date=[]
end_time=[]
end_date=[]

for i in range(1,11):
    BID_NO.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text)
    items.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text)
    Quantity_Required.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text)
    Department_Name_address.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text)
    A.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text)
    b.append(driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text)
    
for items in A:
    Start_date.append(items.split()[0])
    Start_time.append(items.split()[1]+items.split()[2])
for items in b:
    end_date.append(items.split()[0])
    end_time.append(items.split()[1]+items.split()[2])
print(BID_NO)
print(items)
print(Quantity_Required.append)
print(Department_Name_address)
print(Start_date)
print(Start_time)
print(end_date)
print(end_time)
from collections import OrderedDict
col_name = ["BID_NO","items","Quantity_Required","Department_Name_address","Start_date","Start_time","end_date","end_time"]
col_data = OrderedDict(zip(col_name,[BID_NO,items,Quantity_Required,Department_Name_address,Start_date,Start_time,Start_time,end_date,end_time]))
df = pd.DataFrame(col_data) 



