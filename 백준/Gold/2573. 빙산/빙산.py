from collections import deque

def get_ice():
    ice = []

    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 :
                ice.append((i,j))
    return ice

def check(y,x):

    visited = [[False]*m for _ in range(n)]
    q=deque()
    q.append((y,x))
    visited[y][x]=True
    cnt = 0
    while q:
        y,x = q.popleft()
        cnt +=1

        for dy,dx in direction:
            ny,nx = y+dy,x+dx
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
                if  arr[ny][nx]>0:
                    q.append((ny,nx))
                    visited[ny][nx]=True
    
    return cnt

def melt():
    l = []

    for i in ice:
        y,x = i
        temp = 0
        for dy,dx in direction:
            ny,nx = y+dy,x+dx
            if 0<=ny<n and 0<=nx<m and arr[ny][nx]<=0:
                temp +=1
        if temp>0:
            l.append((y,x,temp))

    for y,x,cnt in l :
        arr[y][x] -= cnt



n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

direction = [(1,0),(-1,0),(0,-1),(0,1)]

ice = get_ice()
ans = 0
while ice and check(ice[0][0],ice[0][1]) == len(ice):
    
    ans += 1
    melt()
    ice = get_ice()
    if ice == [] :
        ans = 0
        break

print(ans)