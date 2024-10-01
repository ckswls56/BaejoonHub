from collections import deque


direction = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs():
    
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    
    while q:
        y,x = q.popleft()
        
        
        for dy,dx in direction:
            ny,nx = y+dy,x+dx
            
            if 0<=ny<n and 0<=nx<m and visited[ny][nx] == 0 and board[ny][nx] == 1:
                q.append((ny,nx))
                visited[ny][nx] = visited[y][x] + 1
        
    
    

n,m = map(int,input().split())

board = [list(map(int,input())) for _ in range(n)]

visited = [ list(0 for _ in range(m)) for _ in range(n)]

bfs()

print(visited[n-1][m-1])