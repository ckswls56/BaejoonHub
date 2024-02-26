from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
q = deque()
visited = [[False] * m for _ in range(n)]

q.append((r, c))
cleaned = 0  # 청소한 칸의 개수를 저장할 변수

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서

while q:
    y, x = q.popleft()
    
    if not visited[y][x]:
        visited[y][x] = True
        cleaned += 1  # 로봇이 청소한 칸의 개수를 증가시킴

    # 네 방향 모두 탐색
    for _ in range(4):
        d = (d+3) % 4
        dy, dx = directions[d]
        ny, nx = y + dy, x + dx

        if 0 <= ny < n and 0 <= nx < m and room[ny][nx] == 0 and not visited[ny][nx]:
            q.append((ny, nx))
            break
    else:
        # 네 방향 모두 청소가 이미 되어있거나 벽인 경우 후진
        dy, dx = directions[d]  # 후진 방향 설정
        ny, nx = y - dy, x - dx
        if 0 <= ny < n and 0 <= nx < m and room[ny][nx] == 0:
            q.append((ny, nx))
        else:
            break

print(cleaned)
