n = int(input())
# 오르막 수는 왼쪽의 숫자보다 오른쪽의 숫자가 크거나 같은 수

dp = [[0]*10 for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1
for i in range(2,n+1):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
print(sum(dp[n])%10007)
