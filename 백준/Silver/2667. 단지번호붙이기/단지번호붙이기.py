visited = [[False]*25 for _ in range(25)]
direction = [(0,1),(0,-1),(1,0),(-1,0)]
def dfs(x,y,arr):
    if visited[x][y]:
        return 0
    visited[x][y] = True
    ret = 1
    for dx,dy in direction:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arr[nx][ny] == 1:
            ret += dfs(nx,ny,arr)
    
    return ret


n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int,input().strip()))
answer = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            res = dfs(i,j,arr)
            if res != 0:
                answer.append(res)

print(len(answer))
for i in sorted(answer):
    print(i)

