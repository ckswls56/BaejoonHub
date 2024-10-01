from collections import deque

direction = [(1,0),(-1,0),(0,1),(0,-1)]

# visited 리스트 초기화 메서드
def reset_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False



def bfs(y,x):
    
    q = deque()
    c = board[y][x]
    q.append((y,x))
    visited[y][x] = True
    
    while q:
        y,x = q.popleft()
        
        for dy,dx in direction:
            ny,nx = dy+y,x+dx
            
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                if c == board[ny][nx]:
                    q.append((ny,nx))
                    visited[ny][nx] = True
                    
def bfs_rgb(y,x):
    
    q = deque()
    c = board[y][x]
    q.append((y,x))
    visited[y][x] = True
    
    while q:
        y,x = q.popleft()
        
        for dy,dx in direction:
            ny,nx = dy+y,x+dx
            
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                if c == 'R' or c == 'G':
                    if board[ny][nx] == 'R' or board[ny][nx] == 'G':
                        q.append((ny,nx))
                        visited[ny][nx] = True
                else :
                    if c == board[ny][nx]:
                        q.append((ny,nx))
                        visited[ny][nx] = True



n = int(input())
board = [list(input()) for _ in range(n)]
visited = [list(False for _ in range(n)) for _ in range(n)]

rgb,normal = 0,0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            normal+=1

reset_visited()

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs_rgb(i,j)
            rgb+=1


print(normal,rgb)