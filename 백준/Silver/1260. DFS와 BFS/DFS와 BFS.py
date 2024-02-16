
def dfs(v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in range(1,n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i,visited)

from collections import deque
def bfs(v,visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True

n,m,v = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited = [False]*(n+1)

dfs(v,visited)
print()
visited = [False]*(n+1)
bfs(v,visited)
