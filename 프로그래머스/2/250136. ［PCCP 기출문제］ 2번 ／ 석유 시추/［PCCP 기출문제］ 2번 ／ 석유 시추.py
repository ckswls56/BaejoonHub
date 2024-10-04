from collections import deque

def solution(land):
    answer = 0
    
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # visited 배열 초기화 최적화
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    
    res = [0] * (len(land[0])+1)
    
    # 석유 그룹 탐사
    for i in range(len(land)):
        for j in range(len(land[0])):
            
            if land[i][j] and not visited[i][j]:
                
                cnt = 0
                q = deque([(i, j)])
                visited[i][j] = True
                min_x,max_x = j,j
                
                while q:
                    
                    y, x = q.popleft()
                    min_x,max_x = min(min_x,x),max(max_x,x)
                    cnt+=1
                    
                    for dy, dx in direction:
                        
                        ny, nx = y + dy, x + dx
                        
                        if 0 <= ny < len(land) and 0 <= nx < len(land[0]) and not visited[ny][nx] and land[ny][nx]:
                            q.append((ny, nx))
                            visited[ny][nx] = True
                
                
                for k in range(min_x,max_x+1):
                    res[k] += cnt
                    
    return max(res)
