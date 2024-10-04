import sys
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
dp = [list(0 for _ in range(len(b)+1)) for _ in range(len(a)+1)]


ans = 0 

for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = 0
        
    ans = max(ans,max(dp[i]))
            

print(ans)