# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:50:16 2019

@author: DiPu
"""

import mysql.connector
con=mysql.connector.connect(user="diksha",password='diksha1702',
                            host='db4free.net',database='diksha')
c=con.cursor()
c.execute("""CREATE TABLE student(
        name text,
        age int,
        roll_no int,
        branch text
        )""")
c.execute("INSERT INTO student VALUES ('nEHA',21, 18, 'cs')")
c.execute("INSERT INTO student VALUES ('PRATIK',21, 18, 'IT')")
c.execute("INSERT INTO student VALUES ('pooja',21, 18, 'ec')")
c.execute("INSERT INTO student VALUES ('smita',21, 18, 'IT')")
c.execute("INSERT INTO student VALUES ('saurav',21, 18, 'ec')")
c.execute("INSERT INTO student VALUES ('gaurav',21, 18, 'ee')")
c.execute("INSERT INTO student VALUES ('Ria',21, 18, 'ee')")
c.execute("SELECT * FROM student")

print ( c.fetchall() )


