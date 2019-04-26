# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 22:53:51 2018

@author: nazmul
"""

age = 24
print("My age is " + str(age) + " years.")

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31, 
      "January", "March", "May", "July", "August", "October", "December"))

for i in range (1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

print("Pi is approximately %0.60lf" % (22 / 7))

for i in range (1, 12):
    print("No. {:2} squared is {:4} and cubed is {:4}" .format(i, i ** 2, i ** 3))