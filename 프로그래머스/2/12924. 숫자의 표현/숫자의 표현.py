def solution(n):
    answer = 0
    dp = []
    sum = 0
    for i in range(0,n+1):
        sum+=i
        dp.append(sum)
    
    for i in range(len(dp)-1,0,-1):
        for j in range(i-1,-1,-1):
            if dp[i]-dp[j] == n:
                answer+=1
            if dp[i]-dp[j] > n:
                break
                
    
    return answer