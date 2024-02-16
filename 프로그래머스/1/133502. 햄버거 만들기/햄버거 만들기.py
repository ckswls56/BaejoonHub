from collections import deque


def solution(ingredient):
    answer = 0
    s = deque()
    for i in ingredient:
        if not s:
            s.append(i)
        else :
            if i == 1 and len(s)>= 3:
                if s[-1] == 3 and s[-2] == 2 and s[-3] == 1:
                    s.pop()
                    s.pop()
                    s.pop()
                    answer += 1
                    continue
            s.append(i)
            
    return answer