# -*- coding: utf-8 -*-
"""

Hackerrank Project Euler Problem #3:
The prime factors of 13195 are 5,7,13 and 29.

What is the largest prime factor of a given number N?
Created on Wed Feb 16 20:13:53 2022

@author: onthi
"""
n= 10
i = 2
y =[]
while n >= i:
    if n%i==0:
        y.append(i)
        n=n//i
        i+=1
    else:
        i+=1
print(max(y))
