n = int(input())
arr = [[False]*101 for _ in range(101)]
direction = [(0,1),(-1,0),(0,-1),(1,0)]

for _ in range(n):
    x,y,d,g = map(int,input().split())
    arr[y][x] = True
    curve = [d]

    ## g generation
    for _ in range(g):
        for i in range(len(curve)-1,-1,-1):
            curve.append((curve[i]+1)%4)

    
    for d in curve:
        y,x = y+direction[d][0],x+direction[d][1]
        arr[y][x] = True


res = 0

for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            res +=1

print(res)