n = int(input())
if n == 1:
    print(int(input()))
elif n==2:
    a = int(input())
    b = int(input())
    print(a+b)
elif n==3:
    a = int(input())
    b = int(input())
    c = int(input())
    print(max(a+c,b+c))
else:
    arr = [0] * n
    for i in range(n):
        arr[i] = int(input())
    dp = [0] * n

    dp[0] = (arr[0],arr[0])
    dp[1] = (arr[0]+arr[1],arr[1])

    for i in range(2,n):
        dp[i] = (dp[i-1][1]+arr[i],max(dp[i-2][1]+arr[i],dp[i-2][0]+arr[i]))

    print(max(dp[n-1]))