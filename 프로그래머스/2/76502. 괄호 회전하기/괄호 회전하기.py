from collections import deque

def check(s):
    stack = deque()
    stack.append(s.popleft())

    while stack:
        if stack[-1] in '({[':
            stack.append(s.popleft())
        else:
            if len(stack) < 2:
                return 0
            else:
                r = stack.pop()
                l = stack.pop()
                if not ((l == '[' and r == ']') or (l == '(' and r == ')') or (l == '{' and r == '}')):
                    return 0
            if s:
                stack.append(s.popleft())

    return 1

def solution(s):
    if len(s) % 2 == 1:
        return 0
    stack = deque(s)
    answer = 0
    for i in range(len(s)):
        answer += check(deque(stack))  # Use deque() to create a new deque
        l = stack.popleft()
        stack.append(l)
    return answer
