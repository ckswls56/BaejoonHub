from collections import deque

n,m = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

virus = []
could_virus = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            virus.append((i,j))
            could_virus += 1
        elif a[i][j] == 0:
            could_virus += 1

def combinations(n,arr,new_arr=[], c=0):
    # 순서 상관 X, 중복 X
    result = []
    if len(new_arr) == n:
        result.append(new_arr)
        return result
    for i in range(c, len(arr)):
        result.extend(combinations(n,arr,new_arr + [arr[i]], i + 1))
    return result

def bfs(start_virus):
    q =deque()
    visited = [[-1 for _ in range(n)]for _ in range(n)]
    for v in start_virus:
        # y, x , time
        q.append((v[0],v[1],0))

    #virus spread
    while q:
        y,x,t = q.popleft()

        if visited[y][x] != -1:
            continue

        visited[y][x] = t

        for dy,dx in direction:
            ny,nx = y+dy,x+dx
            if 0<=ny<n and 0<=nx<n and a[ny][nx] != 1:
                if visited[ny][nx] == -1:
                    q.append((ny,nx,t+1))
    temp = 0
    maxs = -1
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1:
                temp += 1
                maxs= max(visited[i][j],maxs)
    
    if temp == could_virus:
        return maxs
    else:
        return -1


combs = combinations(m,virus)
ans = 987654321
for comb in combs :
    sol = bfs(comb)
    if sol != -1:
        ans = min(ans,sol)

if ans != 987654321:
    print(ans)
else :
    print(-1)