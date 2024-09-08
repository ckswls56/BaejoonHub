n = int(input())
find = int(input())

arr = [[-1] * n for _ in range(n)]

# 상, 우, 하, 좌
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

i, j = n // 2, n // 2  # 시작 위치를 배열의 중앙으로 설정
cnt = 1
arr[i][j] = cnt

    
step = 1  # 이동하는 칸 수
direction = 0  # 처음 시작하는 방향 (상)
found_i, found_j = 0, 0  # 찾는 숫자의 위치

while cnt < n * n:
    for _ in range(2):  # 같은 step 크기로 두 번씩 방향을 바꾼다.
        for _ in range(step):
            i += dir[direction][0]
            j += dir[direction][1]
            cnt += 1
            if cnt > n * n:  # 숫자를 모두 채우면 종료
                break
            arr[i][j] = cnt
            if cnt == find:
                found_i, found_j = i, j  # 찾는 숫자의 좌표를 기록
            
        direction = (direction + 1) % 4  # 방향 변경
    step += 1  # 이동하는 칸 수 증가

# 배열 출력
for row in arr:
    print(' '.join(map(str, row)))

# 찾는 숫자의 좌표 출력
if find == 1:
    print(n//2 + 1,n//2 + 1)
else:
    print(found_i+1,found_j+1)