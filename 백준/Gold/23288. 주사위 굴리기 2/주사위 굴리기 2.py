from collections import deque

def right():
    dice[1],dice[2],dice[3],dice[5] = dice[5],dice[1],dice[2],dice[3]

def down():
    dice[0],dice[2],dice[4],dice[5] = dice[5],dice[0],dice[2],dice[4]

def left():
    dice[1],dice[2],dice[3],dice[5] = dice[2],dice[3],dice[5],dice[1]

def up():
    dice[0],dice[2],dice[4],dice[5] = dice[2],dice[4],dice[5],dice[0]



n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# 뒤,왼,위,오,잎,밑
dice = [2,4,1,3,5,6]
# 동 남 서 북
direction = [(0,1),(1,0),(0,-1),(-1,0)]
#시작은 동쪽 시작
d = 0
y,x = 0,0
ans = 0
for _ in range(k):
    dy,dx = direction[d][0],direction[d][1]
    ny,nx = y+dy,x+dx
    if d == 0:
        if 0<=ny<n and 0<=nx<m:
            right()
        else :
            d=(d+2)%4
            left()
            ny,nx = y-dy,x-dx    
    elif d==1:
        if 0<=ny<n and 0<=nx<m:
            down()
        else :
            d=(d+2)%4
            up()
            ny,nx = y-dy,x-dx    
    elif d==2:
        if 0<=ny<n and 0<=nx<m:
            left()
        else :
            d=(d+2)%4
            right()
            ny,nx = y-dy,x-dx    
    elif d==3 :
        if 0<=ny<n and 0<=nx<m:
            up()
        else :
            d=(d+2)%4
            down()
            ny,nx = y-dy,x-dx    

    
    a,b = dice[5],arr[ny][nx]
    
    if a>b:
        d = (d+1)%4
    elif a<b :
        d= (d+3)%4
    
    q = deque()
    q.append((ny,nx))
    visited = [[False for _ in range(m)]for _ in range(n)]
    cnt = 0
    while q :
        r,c = q.popleft()

        if visited[r][c]:
            continue
        visited[r][c] = True
        cnt += 1

        for dr,dc in direction:
            nr,nc = r+dr,c+dc
            if 0<=nr<n and 0<=nc<m:
                if not visited[nr][nc] and arr[nr][nc] == b:
                    q.append((nr,nc))
    
    ans += cnt * b
    y,x = ny,nx
    
print(ans)