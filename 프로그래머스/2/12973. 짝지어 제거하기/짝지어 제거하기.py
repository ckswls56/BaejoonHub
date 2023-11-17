from collections import deque

def solution(s):
    stack = deque()

    string = deque(s)
    if not string:  # 입력 문자열이 비어 있는 경우
        return 1

    stack.append(string.popleft())

    while string:
        char = string.popleft()
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if not stack:
        return 1
    else:
        return 0
