n = int(input())
arr = []


for _ in range(n):
    t, p = map(int, input().split())
    arr.append((t, p))

dp = [0]*n
for i in range(n-1,-1,-1):
    if i+arr[i][0] <= n :
        dp[i] = arr[i][1]
        if dp[i+arr[i][0]:] != [] :
            dp[i] += max(dp[i+arr[i][0]:])

print(max(dp))