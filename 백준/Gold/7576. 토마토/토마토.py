from collections import deque

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs():
    
    q = deque()
    
    for y,x in tomato:
        q.append((y,x))
        # visited[y][x] == 0
    
    
    while q:
        y,x = q.popleft()
        
        for dy,dx in direction:
            ny,nx = y+dy,x+dx
            
            if 0<=ny<n and 0<=nx<m and board[ny][nx] == 0:
                board[ny][nx] = 1
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny,nx))
        
    
    
    
    

def check():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                return True
    
    return False

m,n = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [list(0 for _ in range(m)) for _ in range(n)]
tomato = []
already_done = True

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            tomato.append((i,j))
        elif board[i][j] == 0:
            already_done = False
            
if already_done:
    print(0)
else:
    bfs()
    
    if check():
        print(-1)
    else :
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res,visited[i][j])
                
        print(res)