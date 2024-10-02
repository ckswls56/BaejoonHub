def solve(N):
    # dp 테이블 초기화
    dp = [False] * (N + 1)
    
    # 기본 조건 설정
    if N >= 1:
        dp[1] = True  # 상근이가 이김
    if N >= 2:
        dp[2] = False  # 창영이가 이김
    if N >= 3:
        dp[3] = True  # 상근이가 이김
    
    # 동적 계획법으로 dp 테이블 채우기
    for i in range(4, N + 1):
        # dp[i-1]이나 dp[i-3]에서 창영이가 이기는 상황이 있다면
        # 상근이가 이길 수 있음
        dp[i] = not dp[i-1] or not dp[i-3]
    
    # N개의 돌이 있을 때 누가 이기는지 결과 출력
    if dp[N]:
        print("SK")
    else:
        print("CY")

# 입력 받기
N = int(input())
solve(N)
