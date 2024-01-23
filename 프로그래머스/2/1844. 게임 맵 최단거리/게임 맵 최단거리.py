from collections import deque

direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def bfs(x, y, maps):
    visit = [[False] * (len(maps[0]) + 1) for _ in range(len(maps) + 1)]
    q = deque()
    
    q.append((x, y, 1))
    visit[0][0] = True
    
    while q:
        c_x, c_y, depth = q.popleft()
        
        # Correct the condition here
        if c_x == len(maps) - 1 and c_y == len(maps[0]) - 1:
            return depth
        
        for d_x, d_y in direction:
            next_x = c_x + d_x
            next_y = c_y + d_y
            
            if 0 <= next_x < len(maps) and 0 <= next_y < len(maps[0]):
                if maps[next_x][next_y] and not visit[next_x][next_y]:
                    q.append((next_x, next_y, depth + 1))
                    visit[next_x][next_y] = True
    
    return -1

def solution(maps):
    answer = bfs(0, 0, maps)
    return answer
