def solution(board):
    
    dp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    
    # 첫 행,열 처리
    dp[0] = board[0]
    
    for i in range(len(board)):
        dp[i][0] = board[i][0]
    answer = 0 
    
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]:
                dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
    
    answer = 0
    for i in range(len(dp)):
        answer = max(max(dp[i]),answer)
        
    
    return answer*answer