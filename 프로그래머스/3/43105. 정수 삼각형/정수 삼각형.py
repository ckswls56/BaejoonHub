def solution(triangle):
    dp = [[0]*(x+1) for x in range(len(triangle))]
    
    for i in range(len(triangle[-1])):
        dp[len(triangle)-1][i] = triangle[-1][i]
    

    
    for i in range(len(triangle)-2,-1,-1):
        for j in range(i+1):
            dp[i][j] = max(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
            
    
    answer = dp[0][0]
    return answer