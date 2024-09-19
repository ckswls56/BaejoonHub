

direction = [(-1,0),(1,0),(0,1),(0,-1)]

n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

visited = [list(False for _ in range(m)) for _ in range(n)]


ans = 0

# ㅗ 모양 제외 탐색
def dfs(y,x,sum,cnt):
    global ans
    if cnt == 4:
        ans = max(ans,sum)
        return

    for dy,dx in direction:
        ny,nx = y+dy,x+dx
    
        if 0<=ny<n and 0<=nx<m and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny,nx,sum+board[ny][nx],cnt+1)
            visited[ny][nx] = False


# ㅗ 모양 탐색
def fuck(y,x):
    global ans
    arr = []
    
    for dy,dx in direction:
        ny,nx = y+dy,x+dx
        
        if 0<=ny<n and 0<=nx<m:
            arr.append(board[ny][nx])
    
    if len(arr) == 4:
        arr.sort(reverse=True)
        arr.pop()
        ans = max(ans,sum(arr)+board[y][x])
    elif len(arr) == 3:
        ans = max(ans,sum(arr)+board[y][x])
    else :
        return
    
    
    
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,board[i][j],1)
        fuck(i,j)
        visited[i][j] = False
        
print(ans)