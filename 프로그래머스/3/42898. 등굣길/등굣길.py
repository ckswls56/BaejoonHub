def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif [j+1, i+1] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    
    answer = dp[n-1][m-1]
    return answer