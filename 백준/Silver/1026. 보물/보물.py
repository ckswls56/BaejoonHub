n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
ans = 0
for i,j in zip(a,b):
    ans += i*j
    
print(ans)