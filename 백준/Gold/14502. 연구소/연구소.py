from itertools import combinations
from collections import deque

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(arr):
    q = deque()
    temp = [row[:] for row in arr]  # 깊은 복사 대신 행 단위로 얕은 복사
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i, j))
    
    while q:
        y, x = q.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and temp[ny][nx] == 0:
                temp[ny][nx] = 2
                q.append((ny, nx))
    
    safe = sum(row.count(0) for row in temp)
    return safe

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

zeros = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 0]
walls = list(combinations(zeros, 3))
ans = 0

for wall in walls:
    for y, x in wall:
        board[y][x] = 1
    
    safe_area = bfs(board)
    ans = max(ans, safe_area)
    
    # 벽을 다시 원래 상태로 복구
    for y, x in wall:
        board[y][x] = 0

print(ans)