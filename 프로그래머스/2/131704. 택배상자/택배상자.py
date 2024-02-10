from collections import deque

def solution(order):
    answer = 0
    
    s = deque()
    
    idx = 0
    num = 1
    
    while idx < len(order) :
        if order[idx] == num:
            answer += 1
            idx += 1
            num += 1
        elif s and s[-1] == order[idx]:
            answer += 1
            idx += 1
            s.pop()
        else :
            s.append(num)
            num += 1
            
        if idx<len(order)and order[idx]<num and order[idx] != s[-1]:
            break
            
        
        
    while s and s[-1] == num:
            s.pop()
            answer += 1
            num += 1
    
    return answer