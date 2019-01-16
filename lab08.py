# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:47:46 2019

@author: Faiyaz
"""

    
def find_len(list1): 
    length = len(list1) 
    list1.sort() 
    print("Largest element is:", list1[length-1]) 
    print("Smallest element is:", list1[0]) 
    print("Second Largest element is:", list1[length-2]) 
    print("Second Smallest element is:", list1[1]) 
    print("third Largest element is:", list1[length-3]) 
    print("third Smallest element is:", list1[2]) 
  
# Driver Code 

list = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number '))
    list.append(numbers)
    
Largest = find_len(list) 