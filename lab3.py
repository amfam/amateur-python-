# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:17:22 2019

@author: amir faiyaz
"""

#A copy center charges 50 won per copy for the first 100 copies and 30 won per copy for each additional copy. 
#Write a program that requests the number as input and displays the total cost. 
x=50
y=30
cost=0
i=int(input())
if i<100:
    cost=i*x
    print(cost)
else:
    cost=x*100+y*(i-100)
    
print(cost)    