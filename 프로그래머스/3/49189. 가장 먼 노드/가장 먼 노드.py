from collections import deque
def solution(n, edge):
    
    visit = [-1] * (n+1)
    q = deque()
    g = [[] for _ in range(n+1)]
    
    for s,e in edge :
        g[s].append(e)
        g[e].append(s)
    
    q.append((1,0))
    
    
    while q:
        s,depth = q.popleft()
        
        if visit[s] != -1:
            continue
        
        visit[s] = depth
        
        for e in g[s]:
            if visit[e] == -1:
                q.append((e,depth+1))
                
    longest_distance = max(visit)
    
    answer = list(filter(lambda x : x==longest_distance,visit))
    
    return len(answer)