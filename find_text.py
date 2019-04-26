# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 23:25:19 2017

@author: nazmul
"""
from numpy import array
from block_finder import block_finder

c =  array([17,1,1,3,5,9,0,1,3,17,1,1,5,4,3,1,2,0,12,15,17,1,1,3,4,9,5,7,17,1,1,0,0,0])
#c =  array([17,1,1,3,5,9,17,1,1,2,3,4,7,17,1,1])
j=0

print ("cipher text: ",c)
block_points = []

for i in range (0,len(c)):
    #print(i)
    if c[i] == 17 :
        block_start = block_finder(c,i)
        #print(i)
        #print(block_start)
        
        if block_start == 99999:
            block_points.append(i)
            j=j+1
        
#print(block_start)
print("\nBlock Points : ", block_points)

for i in range (0,len(block_points)):
    if i == len(block_points)-1:
        print("\nBlock Text ",i,": ",c[block_points[i]+3:len(c)])
    
    else:
            print ("\nBlock Text ", i, ": ", c[block_points[i]+3:block_points[i+1]]) 