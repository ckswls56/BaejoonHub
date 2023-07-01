from math import *
n = int(input())
res = [0] * 10

while(n!=0):
    x = n % 10
    n //= 10
    res[x] += 1
temp = res[6]+res[9]
res[6]= ceil((temp)/2)
res[9]= ceil((temp)/2)
print(max(res))