dp = [1] * 10001

t = int(input())

for i in range(2,10001):
    dp[i] += dp[i-2]
    
for i in range(3,10001):
    dp[i] += dp[i-3]
    
    
for _ in range(t):
    n = int(input())
    print(dp[n])