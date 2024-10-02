
T = int(input())

while T:
    T-=1
    
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    
    up_dp = [0 for _ in range(n)]
    down_dp = [0 for _ in range(n)]
    
    up_dp[0] = a[0]
    down_dp[0] = b[0]
    
    for i in range(1,n):
        up_dp[i] = max(up_dp[i-1],a[i]+down_dp[i-1])
        down_dp[i] = max(down_dp[i-1],b[i]+up_dp[i-1])
        
    print(max(up_dp[-1],down_dp[-1]))