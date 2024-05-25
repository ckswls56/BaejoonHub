dp = [-1] * 100

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        if dp[n-1] != -1 and dp[n-2] != 0:
            return dp[n-1]+dp[n-2]
        elif dp[n-1] != -1:
            dp[n-2] = fibonacci(n-2)
            return dp[n-1]+dp[n-2]
        elif dp[n-2] != -1:
            dp[n-1] = fibonacci(n-1)
            return dp[n-1]+dp[n-2]
        else:
            dp[n-1] = fibonacci(n-1)
            dp[n-2] = fibonacci(n-2)
            return dp[n-1]+dp[n-2]
        


t = int(input())

while t:
    n = int(input())
    if n == 0:
        print(1,0)
    else:
        print(fibonacci(n-1),fibonacci(n))
    
    t -= 1