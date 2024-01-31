from collections import deque

def solution(number, k):
    s = deque()
    answer_len = len(number) - k
    num_list = list(map(int, number))
    
    for idx, n in enumerate(num_list):
        if not s:
            s.append(n)
            continue
        
        while s and s[-1] < n and len(number) - idx + len(s) > answer_len:
            s.pop()
        
        s.append(n)
        
        if len(s) == answer_len:
            break
    
    answer = ''.join(map(str, s))
    return answer