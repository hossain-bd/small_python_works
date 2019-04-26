# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:34:59 2018

@author: nazmul
"""

#name = input("Please enter your name: ")
#age = int(input("How old are you, {}? ".format(name)))
#print(age)
#
#if age >=18:
#    print("You are old enough to vote.")
#else:
#    print("Please come back in {0} years.".format(18 - age))

#print("Please guess a number between 1 and 10: ")
#guess = int(input())

#if guess < 5:
#    print("Please guess higher")
#    guess = int(input())
#    if guess == 5:
#        print("Well done, you guessed it")
#    else:
#        print("sorry, you have not guessed correctly.")
#elif guess > 5:
#    print("Please guess lower")
#    guess = int(input())
#    if guess == 5:
#        print("Well done, you guessed it")
#    else:
#        print("Sorry, you have not guessed correctly")
#else:
#    print("You got it first time")

#if guess != 5:
#    if guess < 5:
#        print("Please guess higher")
#    else:
#        print("Please guess lower")
#    
#    guess = int(input())
#    if guess == 5:
#        print("Well done, you guessed it")
#    else:
#        print("Sorry, you have not guessed correctly")
#else:
#    print("You got it first time.")

#age = int(input("How old are you? "))

#if (age >=16) and (age <=65):
#if 16<= age <= 65:
#    print("Have a good day at work")

#if (age <16) or (age >65):
#    print("Enjoy your free time.")
#else:
#    print("Have a good day at work.")

#x = input("Please enter some text ")
#if x:
#    print("You entered '{}'".format(x))
#else:
#    print("You did not enter anything")
#
#print(not False)

age = int(input("How old are you?"))
if not(age >18):
    print("You are old enough to vote")
    print("Please put an X on the box")
else:
    print("Please come back in {} years".format(18 - age))

