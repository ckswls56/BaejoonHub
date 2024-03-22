def dfs(y, x, d):
    if dp[y][x][d] != -1:
        return dp[y][x][d]

    if y == n-1 and x == n-1:
        return 1

    dp[y][x][d] = 0
    
    for dy, dx in direction[d]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 0:
            if dy == 1 and dx == 1:
                if arr[ny-1][nx] == 0 and arr[ny][nx-1] == 0:
                    dp[y][x][d] += dfs(ny, nx, 2)
            elif dy == 1:
                dp[y][x][d] += dfs(ny, nx, 1)
            else:
                dp[y][x][d] += dfs(ny, nx, 0)

    return dp[y][x][d]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)]
direction = [[(0, 1), (1, 1)], [(1, 0), (1, 1)], [(0, 1), (1, 0), (1, 1)]]

print(dfs(0, 1, 0))