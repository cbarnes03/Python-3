# -*- coding: utf-8 -*-
"""
Hackerrank Problem #2:
Each new term in the Fibonacci sequence is generated by adding the previous 
two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed
n, find the sum of the even-valued terms.
Created on Sun Feb 13 22:47:45 2022
@author: Charles Barnes
"""

#Trying to solve via for-loop (probably wont work in event n>>1)
n = 10
sum = 0
x = []
for i in range(1,n):
#how to get odd #'s   i = i+(i-1)
#how to get even #'s  i = i+1
    while i<n:
        x[i] = i+1
    
    