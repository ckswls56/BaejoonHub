def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    i = 1
    y, x = 0, 0
    times = 0
    d = dirs[times]
    while i <= n * n:
        answer[y][x] = i
        ny, nx = y + d[0], x + d[1]
        if ny >= n or ny < 0 or nx >= n or nx < 0 or answer[ny][nx] != 0:
            times += 1
            d = dirs[times % len(dirs)]
        y, x = y + d[0], x + d[1]
        i += 1
    return answer