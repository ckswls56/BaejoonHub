from collections import deque

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(maps,start,target):
    q = deque()
    q.append(start)
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    answer = -1
    
    while q :
        y,x,t = q.popleft()
        
        if y==target[0] and x == target[1]:
            answer = t
            break
        if visited[y][x]:
            continue
            
        visited[y][x] = True
        
        for dy,dx in direction:
            ny,nx = dy+y,x+dx
            if 0<=ny<len(maps) and 0<=nx<len(maps[0]):
                if not maps[ny][nx] == 'X':
                    q.append((ny,nx,t+1))
            
                
    return answer
        
    

def solution(maps):
    answer = 0
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start = (i,j)
            elif maps[i][j] == 'E':
                exit = (i,j)
            elif maps[i][j] == 'L':
                lever = (i,j)
                
    lev_path = bfs(maps,(start[0],start[1],0),(lever[0],lever[1]))
    if lev_path == -1:
        return -1
    
    exit_path = bfs(maps,(lever[0],lever[1],0),(exit[0],exit[1]))
    if exit_path == -1:
        return -1
    
    return lev_path+exit_path