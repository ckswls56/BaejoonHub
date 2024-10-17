from collections import Counter

n, k = map(int, input().split())
arr = list(map(int, input().split()))
c = Counter()

ans = 1
l, r = 0, 0

while r < n:
    # 현재 arr[r] 값이 k개 미만일 때만 오른쪽 포인터를 확장
    if c[arr[r]] < k:
        c[arr[r]] += 1
        r += 1
    else:
        # k개 이상일 경우 왼쪽 포인터를 움직여 슬라이딩 윈도우 축소
        c[arr[l]] -= 1
        l += 1

    # 현재 윈도우 크기를 계산하여 최대값을 갱신
    ans = max(ans, r - l)

print(ans)