import sys
input = sys.stdin.readline

def dfs(start):
    if visited[start]:
        return 0
    stack = [start]
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        for next_node in graph[node]:
            stack.append(next_node)
    return 1

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
answer = 0
for i in range(1, n+1):
    answer += min(dfs(i), 1)

print(answer)
