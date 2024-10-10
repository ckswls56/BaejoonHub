def check(k):
    if len(arr) == 1:
        # arr[0] - k가 0보다 작거나 같고 arr[0] + k가 m보다 크거나 같은지 확인
        return arr[0] - k <= 0 and arr[0] + k >= n
    else:
        # 첫 번째 위치 검사
        if not (arr[0] - k <= 0 and arr[0] + k >= arr[1] - k):
            return False
        
        # 중간 위치 검사
        for i in range(1, m-1):
            if not (arr[i] - k <= arr[i-1] + k and arr[i] + k >= arr[i+1] - k):
                return False
        
        # 마지막 위치 검사
        if not (arr[-1] - k <= arr[-2] + k and arr[-1] + k >= n):
            return False

    return True

n = int(input())  
m = int(input())  
arr = list(map(int, input().split()))  # arr 배열

l, r = 0, n+1  # 이진 탐색 범위 설정

while l < r:
    mid = (l + r) // 2
    if check(mid):
        r = mid
    else:
        l = mid + 1
    
print(r)  # 정답 출력