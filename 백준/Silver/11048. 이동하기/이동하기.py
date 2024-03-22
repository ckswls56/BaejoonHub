import sys
sys.setrecursionlimit(10**7)

def dfs(y, x):
    if dp[y][x] != -1:
        return dp[y][x]

    if y == n-1 and x == m-1:
        return arr[y][x]

    max_path_sum = float('-inf')  # Initialize with negative infinity

    for dy, dx in direction:
        ny, nx = y + dy, x + dx

        if 0 <= ny < n and 0 <= nx < m:
            max_path_sum = max(max_path_sum, dfs(ny, nx))

    dp[y][x] = max_path_sum + arr[y][x]
    return dp[y][x]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
direction = [(1, 0), (0, 1), (1, 1)]
print(dfs(0, 0))