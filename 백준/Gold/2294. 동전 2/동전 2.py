arr = [0]*101
INF = 987654321
dp = [INF]*10001
n, k = map(int, input().split())

for i in range(n):
    arr[i] = int(input())
        
        
dp[0] = 0
for i in range(n):
    coin = arr[i]
    for j in range(coin,k+1):
        if dp[j-coin] != INF:
            dp[j] = min(dp[j],dp[j-coin]+1)
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])