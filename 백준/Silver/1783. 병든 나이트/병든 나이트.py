def solve(N, M):
    # 세로 길이가 1인 경우, 나이트는 움직일 수 없음 (1칸 방문)
    if N == 1:
        return 1
    # 세로 길이가 2인 경우, 나이트는 첫 번째, 네 번째 방법만 사용 가능
    elif N == 2:
        return min(4, (M + 1) // 2)
    # 세로 길이가 3 이상인 경우
    else:
        # 가로 길이가 7보다 작으면 최대 4칸까지 이동 가능 (모든 방법 사용 불가)
        if M < 7:
            return min(4, M)
        # 가로 길이가 7 이상이면 모든 방법을 사용하고 나머지는 오른쪽으로만 이동
        else:
            return M - 2

# 입력 처리
N, M = map(int, input().split())
print(solve(N, M))
