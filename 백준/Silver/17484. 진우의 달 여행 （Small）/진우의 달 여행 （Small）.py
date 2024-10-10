
# 갈 수 있는 방향
direction = [(1,-1),(1,0),(1,1)]


def dfs(y,x,d,total):
    if y == n-1:
        
        return total + board[y][x]
    
    ret = 10000
    
    for i in range(3):
        if i==d:
            continue
        dy,dx = direction[i][0],direction[i][1]
        ny,nx = dy+y,dx+x
        if 0<=ny<n and 0<=nx<m :
            ret = min(ret,dfs(ny,nx,i,total+board[y][x]))
            
    
    return ret
        
n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]


ans = 10000

for j in range(m):
    for i in range(3):
        dy,dx = direction[i][0],direction[i][1]
        ny,nx = dy,dx+j
        if 0<=ny<n and 0<=nx<m :
            ans = min(ans,dfs(ny,nx,i,board[0][j]))
            
            
print(ans)