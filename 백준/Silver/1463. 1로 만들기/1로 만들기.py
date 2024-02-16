from collections import deque

N = int(input())
q = deque()
q.append((N, 0))
visited = [False] * 1000001
visited[N] = True

while q:
    x, cnt = q.popleft()
    if x == 1:
        print(cnt)
        break
    if x % 3 == 0 and not visited[x // 3]:
        q.append((x // 3, cnt + 1))
        visited[x // 3] = True
    if x % 2 == 0 and not visited[x // 2]:
        q.append((x // 2, cnt + 1))
        visited[x // 2] = True
    if not visited[x - 1]:
        q.append((x - 1, cnt + 1))
        visited[x - 1] = True
