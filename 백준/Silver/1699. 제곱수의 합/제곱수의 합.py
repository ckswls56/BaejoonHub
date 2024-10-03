n = int(input())

dp = [10000] * (n + 1)

dp[0] = 0  # 0은 제곱수 합이 0이므로 0으로 설정

for i in range(1, n + 1):
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])
