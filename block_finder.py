# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 23:39:31 2017

@author: nazmul
"""

def block_finder(c,i):
    block_start = 0
    #print(c)
    if c[i+1] == 1 :
        if c[i+2] == 1:
            block_start = 99999
        else:
            block_start = 77777
    else:
       block_start = 77777
    
     #if c[i] == 1:
            #block_start = True
    
    return block_start
    