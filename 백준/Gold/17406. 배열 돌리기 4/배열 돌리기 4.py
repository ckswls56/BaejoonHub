from itertools import permutations
from collections import deque
import copy

# 각 행의 합 중 최솟값을 구하는 함수
def get_min(arr):
    res = float('inf')
    for row in arr:
        res = min(res, sum(row))
    return res

# 배열을 회전시키는 함수
def rotate_arr(arr, r, c, s):
    for layer in range(1, s + 1):
        top_left = (r - layer, c - layer)
        bottom_right = (r + layer, c + layer)
        
        q = deque()
        
        # 윗변
        for i in range(top_left[1], bottom_right[1]):
            q.append(arr[top_left[0]][i])
        
        # 오른쪽 변
        for i in range(top_left[0], bottom_right[0]):
            q.append(arr[i][bottom_right[1]])
        
        # 아랫변
        for i in range(bottom_right[1], top_left[1], -1):
            q.append(arr[bottom_right[0]][i])
        
        # 왼쪽 변
        for i in range(bottom_right[0], top_left[0], -1):
            q.append(arr[i][top_left[1]])
        
        # 시계 방향으로 한 칸 회전
        q.rotate(1)
        
        # 다시 배열에 값 복사
        # 윗변
        for i in range(top_left[1], bottom_right[1]):
            arr[top_left[0]][i] = q.popleft()
        
        # 오른쪽 변
        for i in range(top_left[0], bottom_right[0]):
            arr[i][bottom_right[1]] = q.popleft()
        
        # 아랫변
        for i in range(bottom_right[1], top_left[1], -1):
            arr[bottom_right[0]][i] = q.popleft()
        
        # 왼쪽 변
        for i in range(bottom_right[0], top_left[0], -1):
            arr[i][top_left[1]] = q.popleft()

# 입력 처리
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rotations = [list(map(int, input().split())) for _ in range(k)]

# 최솟값을 찾기 위한 변수
ans = float('inf')

# 모든 회전 순서를 고려
for perm in permutations(range(k)):
    temp_arr = copy.deepcopy(arr)
    
    # 각 순열에 따라 회전 수행
    for p in perm:
        r, c, s = rotations[p]
        rotate_arr(temp_arr, r - 1, c - 1, s)
    
    # 회전 결과의 최소 행 합 계산
    ans = min(ans, get_min(temp_arr))

# 결과 출력
print(ans)