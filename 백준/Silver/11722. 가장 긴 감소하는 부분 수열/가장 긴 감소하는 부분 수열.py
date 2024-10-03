
n = int(input())
arr = list(map(int,input().split()))

dp = [0 for _ in range(n)]

dp[0] = 1

for i in range(1,n):
    j = i-1
    while j >= 0:
        if arr[i]<arr[j]:
            dp[i]= max(dp[i],dp[j]+1)
            
        j-=1
        
    if dp[i] == 0:
        dp[i] = 1  

print(max(dp))