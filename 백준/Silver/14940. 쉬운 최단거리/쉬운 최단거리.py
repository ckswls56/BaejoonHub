
from collections import deque
direction = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(s_y,s_x):
    q = deque()
    q.append((s_y,s_x))
    visited = [[-1]*m for _ in range(n)]
    visited[s_y][s_x] = 0
    while q:
        y,x = q.popleft()
        
        for dy,dx in direction:
            ny,nx = y+dy,x+dx
            
            if 0<=ny<n and 0<= nx < m and visited[ny][nx] == -1:
                if arr[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny,nx))
        
    return visited        

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            y,x = i,j
            

res = bfs(y,x)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 :
            res[i][j] = 0
            

for r in res:
    print(*r)