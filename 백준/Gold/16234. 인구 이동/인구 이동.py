from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    group = [(y, x)]
    total_population = a[y][x]
    visited[y][x] = True

    while q:
        y, x = q.popleft()

        for dy, dx in dir:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and l <= abs(a[ny][nx] - a[y][x]) <= r:
                q.append((ny, nx))
                visited[ny][nx] = True
                group.append((ny, nx))
                total_population += a[ny][nx]

    return group, total_population

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0

while True:
    visited = [[False] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group, total_population = bfs(i, j)
                group_size = len(group)
                if group_size > 1:
                    moved = True
                    avg_population = total_population // group_size
                    for y, x in group:
                        a[y][x] = avg_population

    if not moved:
        break
    else:
        ans += 1

print(ans)