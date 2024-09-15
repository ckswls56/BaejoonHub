# 입력 받기
n, m = map(int, input().split())  # n: 스크린 크기, m: 바구니 크기
j = int(input())  # 떨어지는 사과의 개수

# 바구니의 처음 위치는 1번 칸에서 m칸을 차지
left = 1  # 바구니의 왼쪽 끝 위치
right = m  # 바구니의 오른쪽 끝 위치

# 최소 이동 거리
ans = 0

for _ in range(j):
    apple = int(input())  # 사과가 떨어지는 위치
    
    # 사과가 바구니 안에 들어오는지 확인
    if left <= apple <= right:
        continue  # 바구니가 사과 위치를 포함하면 이동할 필요 없음
    
    # 사과가 바구니의 왼쪽보다 왼쪽에 떨어지면 바구니를 왼쪽으로 이동
    if apple < left:
        move = left - apple  # 왼쪽으로 이동해야 하는 거리
        left -= move
        right -= move
        ans += move
    
    # 사과가 바구니의 오른쪽보다 오른쪽에 떨어지면 바구니를 오른쪽으로 이동
    elif apple > right:
        move = apple - right  # 오른쪽으로 이동해야 하는 거리
        left += move
        right += move
        ans += move

# 최종 이동 거리 출력
print(ans)