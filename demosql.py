# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 22:54:16 2018

@author: nazmul
"""

import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='virtual_power_plant')

a = conn.cursor()

###############################################################################
"""
Define The buttons:
"""

solar = 'SELECT * from `solar`;'
wind = 'SELECT * from `wind`;'
newclear = 'SELECT * from `newclear`;'
coal = 'SELECT * from `coal`;'
###############################################################################

a.execute(solar)

countrow = a.execute(solar)
print("Number of rows :",countrow)
data = a.fetchone()

print ("\n###########################################################")
print ("List of solar Power plants in the Rakib virtual Power Plant:")

print ("###########################################################\n")
print ("The name of the power plant is:",data[0])
print ("Power generation capacity:",data[1])
print ("Date of acquisition:",data[2])
print ("Purchase price of the plant:",data[3],'Million')
print ("Plant location:",data[4])
print ("The plant is in operation for",data[5],'hours')
print ("Identification Number:",data[6])

#value = float(data[solar]) # load the data into value with conversion of its type

###############################################################################
"""
Check a certain value from a row and then select that row
"""

myName = 'Dip Power'
a.execute("SELECT * FROM solar WHERE name=%s", (myName,))

data = a.fetchone()
print ("\nThe capacity of the", data[0], 'is :',data[1], 'Mega Watt')

###############################################################################
"""
Update a new row of a table (create a new record)
"""
#a.execute("INSERT INTO `wind` (`name`, `power`, `dateacq`, `price`, `location`, `operate_time`, `id`) VALUES (%s, %s, %s, %s, %s, %s, %s)",  ('rakib power', '45', '26th January, 1986', '23', 'Koln', '324', 'CX3455jh573a'))
#conn.commit()
#conn.close()

###############################################################################

