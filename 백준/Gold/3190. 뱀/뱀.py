from collections import deque

n = int(input())
k = int(input())
board = [[False]*101 for _ in range(101)]

for i in range(k):
    y,x = map(int,input().split())
    board[y][x] = True

l = int(input())
command = {}

for i in range(l):
    s = input().split()
    x,c = int(s[0]),s[1]
    command[x] = c

dir = [(0,1),(1,0),(0,-1),(-1,0)] # 오른쪽,밑,왼쪽,위

snake = deque([(1, 1)])  # 뱀의 머리 위치를 저장하는 deque
time = 0
d = 0
while True:
    time += 1
    y, x = snake[-1]  # 뱀의 머리 위치
    ny, nx = y + dir[d][0], x + dir[d][1]  # 다음 머리 위치
    if 1 <= ny <= n and 1 <= nx <= n and (ny, nx) not in snake:  # 벽에 부딪히거나 자기 자신의 몸통과 충돌하지 않는 경우
        snake.append((ny, nx))  # 뱀의 머리 위치 갱신
        if not board[ny][nx]:  # 사과가 없는 경우
            snake.popleft()  # 꼬리 자르기
        else:
            board[ny][nx] = False  # 사과를 먹은 경우 보드에서 사과 제거
    else:  # 벽에 부딪히거나 자기 자신의 몸통과 충돌한 경우
        break
    
    if time in command:
        if command[time] == 'L':
            d = (d+3) % 4
        else:
            d = (d+1) % 4

print(time)
