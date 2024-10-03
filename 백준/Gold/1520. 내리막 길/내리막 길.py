import sys
sys.setrecursionlimit(10**6)

direction = [(-1,0),(1,0),(0,-1),(0,1)]


def dfs(y,x):
    
    if(y==n-1 and x==m-1):
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0
    
    for dy,dx in direction:
        ny,nx = y+dy,x+dx
        if 0<=ny<n and 0<=nx<m and board[y][x]>board[ny][nx]:
            dp[y][x] += dfs(ny,nx)
    
    
    return dp[y][x]

n,m = map(int,input().split())

board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [list(-1 for _ in range(m+1)) for _ in range(n+1)]

print(dfs(0,0))