# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:27:23 2019

@author: amir faiyaz
"""

#5. A calendar year divisible by four is a leap year, with the exception of the years ending in 00 (that is, those divisible by 100) and not divisible by 400. For instance the years 1600 and 2000 are leap years, but 1700, 1800, and 1900 are not. 
#Write a program that requests a year as input and states whether it is a leap year
print('Enter year')
i=int(input())
if(i<400 & i%4==0):
    print(i,'is a leap year')
elif(i%400==0):
    print(i,'is a leap year')
else:
    print(i,"is not leap year")
    
