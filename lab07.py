# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:40:11 2019

@author: Faiyaz
"""

#7. A person born in 1980 can claim, &quot;I will be x years old in the year x squared.&quot; &#39;. What is the value of x?
#Hints: It forms a quadratic equation X^2-X-1980=0
import cmath
c=1980

r=(-1)**2-4*1*c
sol1 = (-1-cmath.sqrt(r))/(2*1)
sol2 = (-1+cmath.sqrt(r))/(2*1)

print('The solution are {0} and {1}'.format(sol1,sol2))
#ans=1+r/2*1*-1
#print(ans)