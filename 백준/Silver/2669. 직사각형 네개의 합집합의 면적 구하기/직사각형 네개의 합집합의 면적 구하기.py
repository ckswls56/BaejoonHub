arr = [[False for _ in range(103)]for _ in range(103)]

for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j]=True

ans = 0
for i in range(102):
    for j in range(102):
        if arr[i][j]:
            ans+=1
print(ans)