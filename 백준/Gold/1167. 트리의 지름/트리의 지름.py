import sys
input = sys.stdin.readline

def dfs(s, sumation):
    global max_node,max_dist
    visited[s] = True
    if sumation > max_dist :
        max_node,max_dist = s ,sumation
    
    for next_node in g[s]:
        next, weight = next_node
        if not visited[next]:
           dfs(next, sumation + weight)

v = int(input())

g = [[] for _ in range(v+1)]
visited = [False] * (v+1)
for i in range(1, v+1):
    s = list(map(int, input().split()))
    for j in range(1, len(s), 2):
        if s[j] == -1:
            break
        g[s[0]].append((s[j], s[j+1]))

max_node,max_dist = None,0
answer = 0
visited[1] = True
dfs(1, 0)
visited = [False] * (v+1)
visited[max_node] = True
dfs(max_node,0)
    
print(max_dist)
