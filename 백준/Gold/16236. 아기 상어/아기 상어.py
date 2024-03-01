from collections import deque

def bfs(start, size):
    q = deque()
    y = start[0]
    x = start[1]
    q.append((y, x, 0))
    visited = [[False] * n for _ in range(n)]
    possible = []

    while q:
        y, x, distance = q.popleft()

        if visited[y][x]:
            continue

        if 0 < arr[y][x] < size:  # 먹이가 있고 상어가 먹을 수 있는 크기보다 작은 경우
            possible.append((y, x, distance))

        visited[y][x] = True

        for dy, dx in ((1, 0), (0, -1), (-1, 0), (0, 1)):
            ny = dy + y
            nx = dx + x

            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if size >= arr[ny][nx]:
                    q.append((ny, nx, distance + 1))

    return possible

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            start = (i, j)
            arr[i][j] = 0  # 상어가 있는 자리는 빈 공간으로 표시

size = 2
exp = 0  # 상어가 먹은 먹이의 수
answer = 0

while True:
    possible = bfs(start, size)

    if not possible:
        break

    possible.sort(key=lambda x: (x[2], x[0], x[1]))
    y, x, distance = possible[0]

    answer += distance
    exp += 1

    if exp == size:
        size += 1
        exp = 0

    start = (y, x)
    arr[y][x] = 0

print(answer)
