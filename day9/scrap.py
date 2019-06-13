# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:52:04 2019

@author: DiPu
"""
from bs4 import BeautifulSoup
import requests
import sqlite3
odi="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source=requests.get(odi).text
soup = BeautifulSoup(source,"lxml")
right_table=soup.find('table', class_="table")
print(right_table)
A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
con=sqlite3.connect("student.db")
c=con.cursor()
c.execute("""create table crickets(
        ranking text,
        country text,
        weighted_match text,
        point text,
        ratings text)""")
for i in range(0,len(A)):
    c.execute("insert into crickets values("+A[i]+" ,'"+B[i]+"', '"+C[i]+"' , '"+D[i]+"' , '"+E[i]+"' )")

print(c.fetchall())
    
    


