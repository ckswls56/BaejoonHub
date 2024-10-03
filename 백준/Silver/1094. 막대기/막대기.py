
x = int(input())

ans = 0

for i in range(7):
    if x & (1<<i):
        ans+=1
        
print(ans)