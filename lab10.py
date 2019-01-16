# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:08:55 2019

@author: Faiyaz
"""
import math
a1=int(input('left side of triangle: '))
a2=int(input('left side of triangle: '))
f=int(input('floor of triangle: '))
h=math.sqrt(a1**2-(f/2)**2) #finding height using : a^2=b^2+c^2
print("area of a triangle :",1/2*h*f)
