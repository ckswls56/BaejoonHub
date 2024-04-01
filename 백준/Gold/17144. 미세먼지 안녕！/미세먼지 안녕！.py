import sys
input = sys.stdin.readline

r,c,t = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(r)]
direction = [(1,0),(-1,0),(0,-1),(0,1)]

# 공기청정기 좌표 구하기
for j in range(1):
    for i in range(r-1):
        if a[i][j]==-1 and a[i+1][j] == -1:
            cleaner_y = i,i+1

while t:
    t-=1

    temp = {}

    #Spread
    for i in range(r):
        for j in range(c):
            if a[i][j]>=5:
                cnt = 0
                for dy,dx in direction:
                    ny,nx = i+dy,j+dx
                    if 0<=ny<r and 0<=nx<c and a[ny][nx] != -1:
                        if (ny,nx) in temp :
                            temp[(ny,nx)] = temp[(ny,nx)] + a[i][j]//5
                        else :
                            temp[(ny,nx)] = a[i][j]//5
                        cnt += 1
                a[i][j] -= cnt * (a[i][j]//5)

    for k,v in temp.items():
        y,x = k
        a[y][x] += v
    
    #Air purifier 
    y,x,dir = cleaner_y[0]-1,0,0
    while a[y][x] != -1:
        if dir == 0:
            if y-1 >=0 :
                y-=1
                a[y+1][x] = a[y][x]
            else:
                dir += 1
                continue
        elif dir == 1:
            if x+1 < c :
                x+=1
                a[y][x-1] = a[y][x]
            else :
                dir += 1
        elif dir == 2:
            if y+1 <= cleaner_y[0]:
                y+=1
                a[y-1][x] = a[y][x]
            else:
                dir += 1
        else :
            if x-1 > 0:
                x-=1
                a[y][x+1]=a[y][x]
            else:
                a[y][x] = 0
                break
    
    y,x,dir = cleaner_y[1]+1,0,0
    while a[y][x] != -1:
        if dir == 0:
            if y+1 < r:
                y+=1
                a[y-1][x] = a[y][x]
            else:
                dir += 1
                continue
        elif dir == 1:
            if x+1 < c :
                x+=1
                a[y][x-1] = a[y][x]
            else :
                dir += 1
        elif dir == 2:
            if y-1 > cleaner_y[0]:
                y-=1
                a[y+1][x] = a[y][x]
            else:
                dir += 1
        else :
            if x-1 > 0:
                x-=1
                a[y][x+1]=a[y][x]
            else:
                a[y][x] = 0
                break
        

ans = 0
for i in range(r):
    for j in range(c):
        if a[i][j]>0:
            ans += a[i][j]

print(ans)
