import sys
from collections import deque

# 초기 입력
q = list(input())
m = int(input())

# 커서 왼쪽에 있는 문자는 left_stack, 오른쪽 문자는 right_stack으로 나눔
left_stack = deque(q)
right_stack = deque()

# 명령어 처리
for _ in range(m):
    command = sys.stdin.readline().rstrip()
    
    if command[0] == 'P':  # 문자 삽입
        _, x = command.split()
        left_stack.append(x)
    elif command == 'L':  # 커서를 왼쪽으로 이동
        if left_stack:
            right_stack.appendleft(left_stack.pop())
    elif command == 'D':  # 커서를 오른쪽으로 이동
        if right_stack:
            left_stack.append(right_stack.popleft())
    elif command == 'B':  # 문자 삭제
        if left_stack:
            left_stack.pop()

# 결과 출력
print("".join(left_stack) + "".join(right_stack))