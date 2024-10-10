n, x = map(int, input().split())
visited = list(map(int, input().split()))

# 누적합을 저장할 배열
dp = [0] * (n+1)

# 누적합 계산
for i in range(1, n+1):
    dp[i] = dp[i-1] + visited[i-1]

ans = 0
cnt = 0

# x일 동안 가장 많은 방문자 수를 찾음
for i in range(x, n+1):
    s = dp[i] - dp[i-x]
    if s > ans:
        ans = s
        cnt = 1
    elif s == ans:
        cnt += 1

# 출력
if ans > 0:
    print(ans)
    print(cnt)
else:
    print("SAD")
