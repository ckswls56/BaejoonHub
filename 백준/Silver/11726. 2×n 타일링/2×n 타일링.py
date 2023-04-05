n = int(input())

if n==1:
    print(1)
elif n == 2:
    print(2)
else :
    res= list()
    res.append(1)
    res.append(2)
    for i in range(2,n) :
        res.append((res[i-1]+res[i-2])%10007)
    print(res[-1])