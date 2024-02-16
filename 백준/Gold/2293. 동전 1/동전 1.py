arr = [0]*101
dp = [0]*10001
n, k = map(int, input().split())

for i in range(n):
    arr[i] = int(input())
        
dp[0] = 1
for i in range(n):
    for j in range(arr[i],k+1):
        dp[j] += dp[j-arr[i]]

print(dp[k])
