
n = int(input())
arr = list(map(int,input().split()))

dp = [0 for _ in range(n)]

dp[0] = arr[0]

for i in range(1,n):
    j = i-1
    while j >= 0:
        if arr[i]>arr[j]:
            dp[i]= max(dp[i],dp[j]+arr[i])
            
        j-=1
        
    if dp[i] == 0:
        dp[i] = arr[i]        

print(max(dp))