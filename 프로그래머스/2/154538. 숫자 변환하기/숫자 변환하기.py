from collections import deque

def solution(x, y, n):
    answer = -1
    q = deque()
    q.append((x,0))
    visit = [False] * 1000001
    while q:
        x,times = q.popleft()
        if visit[x] :
            continue
        
        if x == y:
            return times
        visit[x] = True
        if x+n < 1000001:
            q.append((x+n,times+1))
        if x*2 < 1000001:
            q.append((x*2,times+1))
        if x*3 < 1000001:
            q.append((x*3,times+1))
        
        
    return answer