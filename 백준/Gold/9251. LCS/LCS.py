a = list(input())
b = list(input())

dp = [list(0 for _ in range(1001)) for _ in range(1001)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(max(dp[len(a)-1]))