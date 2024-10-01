def sol(times, summation):
    if times == n:  # 수열의 끝까지 확인했다면
        return 1 if summation == s else 0  # 합이 S일 때 1을 반환
    
    # 현재 원소를 선택하지 않은 경우와 선택한 경우로 나누어서 재귀적으로 계산
    ret = sol(times + 1, summation) + sol(times + 1, summation + arr[times])
    
    return ret

n, s = map(int, input().split())
arr = list(map(int, input().split()))

# 결과는 부분수열의 크기가 양수인 경우이므로 초기 값을 0에서 빼준다.
result = sol(0, 0)
if s == 0:  # 합이 0인 경우는 빈 부분수열이 포함될 수 있으므로 1을 빼줌
    result -= 1

print(result)