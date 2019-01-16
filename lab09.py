# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:56:10 2019

@author: Faiyaz
"""

list = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    list.append(numbers)
add=sum(list)
length = len(list) 
aver=add/num
list.sort()
ldif=aver-list[length-1]
sdif=aver-list[0]

print("the difference between average and a)smallest element",sdif ,"and b)largest",ldif)