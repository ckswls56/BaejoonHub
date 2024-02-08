def solution(land):
    
    dp = [[0]*4 for _ in range (len(land))]
    
    for i in range(1):
        for j in range(4):
            dp[i][j] = land[i][j]
    
    
    for i in range(1,len(land)):
        for j in range(4):
            if j == 0:
                dp[i][j] = max(dp[i-1][1],dp[i-1][2],dp[i-1][3]) + land[i][j]
            elif j == 1:
                dp[i][j] = max(dp[i-1][0],dp[i-1][2],dp[i-1][3]) + land[i][j]
            elif j == 2:
                dp[i][j] = max(dp[i-1][0],dp[i-1][1],dp[i-1][3]) + land[i][j]
            else :
                dp[i][j] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2]) + land[i][j]
    
    return max(dp[len(land)-1])
