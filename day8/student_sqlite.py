# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:07:46 2019

@author: DiPu
"""

import os
import sqlite3
from pandas import DataFrame
conn = sqlite3.connect ( 'students.db' )
c=conn.cursor()
c.execute("""CREATE TABLE STUDENT(Student_Name TEXT,
                                  Student_Age int, 
                                  Student_Roll_no INT, 
                                  Student_Branch TEXT
        )""")
add_table ('Diksha',21, 18, 'IT')
c.execute("INSERT INTO student VALUES ('nEHA',21, 18, 'cs')")
c.execute("INSERT INTO student VALUES ('PRATIK',21, 18, 'IT')")
c.execute("INSERT INTO student VALUES ('pooja',21, 18, 'ec')")
c.execute("INSERT INTO student VALUES ('smita',21, 18, 'IT')")
c.execute("INSERT INTO student VALUES ('saurav',21, 18, 'ec')")
c.execute("INSERT INTO student VALUES ('gaurav',21, 18, 'ee')")
c.execute("INSERT INTO student VALUES ('Ria',21, 18, 'ee')")
c.execute("SELECT * FROM student")
print ( c.fetchall() )

