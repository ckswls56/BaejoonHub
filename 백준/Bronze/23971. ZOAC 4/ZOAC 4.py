h,w,n,m = map(int,input().split())

direction = [(-1,0),(1,0),(0,-1),(0,1)]

ans = 0
for i in range(0,h,n+1):
    for j in range(0,w,m+1):
        ans += 1
        
print(ans)   