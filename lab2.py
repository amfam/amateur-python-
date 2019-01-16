# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:13:41 2019

@author: amir faiyaz
"""

#3.Write a program that asks the user to enter a whole number of inches and convert that length to feet and inches. See the following figure. The program should use both integer division and the modulus operator. 
inch=int(input())
feet=int(inch/12)
inches=int(inch)%12
print(inch ,"inches if ",feet,"feet","and",inch,"inches")
