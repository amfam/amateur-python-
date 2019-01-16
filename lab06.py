# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:06:31 2019

@author: Faiyaz
"""

#6. Print average of all numbers divisible by 3 and less than 100.
print('average of numbers which are divisible by 3')
su=0
count=0
for i in range(3,100,3):
    su+=i
    count+=1
print(su/count)    
