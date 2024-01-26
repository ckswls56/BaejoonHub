from collections import deque
def solution(numbers):
    
    stack = deque()
    answer = [-1] * len(numbers)
    

    stack.append(0)
    for i in range(1, len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer