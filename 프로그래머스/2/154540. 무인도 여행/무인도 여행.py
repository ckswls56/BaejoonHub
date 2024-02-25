from collections import deque

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y, maps, visited):
    queue = deque([(x, y)])
    visited[y][x] = True
    total = 0
    
    while queue:
        cx, cy = queue.popleft()
        if maps[cy][cx] != 'X':
            total += int(maps[cy][cx])
        
        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx] != 'X' and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny))
                
    return total

def solution(maps):
    answer = []
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs(j, i, maps, visited))
                
    answer.sort()
    if answer == []:
        return [-1]
    return answer
