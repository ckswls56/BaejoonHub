n= int(input())
dp =[1]*(100000+1)
dp[1] = 3
dp[2] = 7


for i in range(3,n+1):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-1])%9901

print(dp[n])