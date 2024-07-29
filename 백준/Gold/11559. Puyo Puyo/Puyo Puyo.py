from collections import deque


COLOR = ['R','G','B','P','Y']
direction = [(-1,0),(1,0),(0,-1),(0,1)]

# bfs 로 탐색하여 상하좌우 4개 이상이면 반환한다
def bfs(sy,sx,color):
    
    ret = set()
    ret.add((sy,sx))
    q = deque()
    q.append((sy,sx))
    
    while q:
        y,x = q.popleft()
        
        if visited[y][x]:
            continue
        
        visited[y][x] = True
        
        for dy,dx in direction:
            cy,cx = y+dy,x+dx
            
            if 0<=cy<12 and 0<=cx<6 and not visited[cy][cx] and color == board[cy][cx]:
                q.append((cy,cx))
                ret.add((cy,cx))
                
    
    if len(ret)>= 4:
        return ret
    else :
        return None
                


def gravity():
    for i in range(10,-1,-1):
        for j in range(6):
            if board[i][j] != '.':
                k = i + 1
                while k < 12 and board[k][j] == '.':
                    k += 1
                # Swap the current cell with the lowest empty spot found
                if k > i + 1:
                    board[k - 1][j], board[i][j] = board[i][j], board[k - 1][j]





board = [list(input()) for _ in range(12)]
visited = [[False]*6 for _ in range(12)]


ans = 0

while True:
    chains=[]
    
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                chain = bfs(i,j,board[i][j])
                if chain != None:
                    chains.append(chain)
                    
    if not chains:
        break
    
    for chain in chains:
        for y,x in chain:
            board[y][x] = '.'
            
    
    gravity()
    visited = [[False]*6 for _ in range(12)]
    

    ans += 1
    
print(ans)