from collections import deque

def solution(priorities, location):
    answer = 1
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
        
    while True :
        flag = False
        p = q.popleft()
        for x in q:
            if x[0]>p[0]:
                flag = True
                break
        if flag :
            q.append(p)
        elif p[1] == location:
            return answer
        else :
            answer+=1
    