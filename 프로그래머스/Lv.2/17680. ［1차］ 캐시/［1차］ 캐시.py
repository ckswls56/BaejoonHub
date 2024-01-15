from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()

    
    for c in cities:
        c = c.lower()
        if c in q:
            answer +=1
            q.remove(c)
            q.append(c)
        else :
            q.append(c)
            if len(q)>cacheSize :
                q.popleft()
            answer+=5
        
    
    return answer