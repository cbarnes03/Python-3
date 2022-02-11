"""
Created on Fri Feb 11 13:48:48 2022
author: Charles Barnes
"""

n=100
#starting idea
# sum =0
# x = []
# for i in range (1,n):
#     if i % 3==0 or i % 5==0:
#         x.append(i)
#         sum+=i
# print(sum)

#optimized equation for above
n = n-1        
y = ((n//3)*(2*3+(n//3-1)*3)//2)
z = ((n//5)*(2*5+(n//5-1)*5)//2)
a = ((n//15)*(2*15+(n//15-1)*15)//2)
b = y+z-a
print(b)


