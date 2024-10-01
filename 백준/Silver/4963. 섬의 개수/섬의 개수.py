from collections import deque

direction = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]


def bfs(y,x):
    q = deque()
    
    q.append((y,x))
    visited[y][x] = True
    
    while q:
        y,x = q.popleft()
        
        for dy,dx in direction:
            ny,nx = dy+y,dx+x
            
            if 0<=ny<h and 0<=nx<w and not visited[ny][nx] and board[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((ny,nx))
                

w,h = map(int,input().split())

while not(w == 0 and h == 0):
    board = [list(map(int,input().split())) for _ in range(h)]
    visited = [list(False for _ in range(w)) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                ans += 1
    print(ans)
    w,h = map(int,input().split())