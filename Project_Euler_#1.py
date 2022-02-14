"""
Hackerrank Project Euler Problem #1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below n.
Created on Fri Feb 11 13:48:48 2022
@author: Charles Barnes
"""
#test case for n
n = 100

#starting idea but times out in n>>1
# sum =0
# x = []
# for i in range (1,n):
#     if i % 3==0 or i % 5==0:
#         x.append(i)
#         sum+=i
# print(sum)

#optimized solution
n = n-1        
mul3 = (n//3) * (2 * 3 + (n//3-1) * 3) //2
mul5 = (n//5) * (2 * 5+ (n//5-1) * 5) //2
overlap = (n//15) * (2 * 15+(n//15-1) * 15) //2
total = mul3 + mul5 - overlap
print(total)


