
a,b = map(int,input().split())

m = int(input())


sum = 0

arr = list(map(int,input().split()))


for x in arr:
    sum += x * (a ** (m-1))
    
    m-=1
    

ans = []

while sum > 0:
    
    ans.append(sum%b)
    sum //= b

ans.reverse()

print(*ans)