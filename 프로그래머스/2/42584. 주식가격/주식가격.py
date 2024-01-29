from collections import deque

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = deque()

    for i in range(len(prices)):
        while stack and stack[-1][0] > prices[i]:
            x = stack.pop()
            answer[x[1]] = i - x[1]
        stack.append((prices[i], i))

    while stack:
        x = stack.pop()
        answer[x[1]] = len(prices) - x[1] - 1

    return answer
