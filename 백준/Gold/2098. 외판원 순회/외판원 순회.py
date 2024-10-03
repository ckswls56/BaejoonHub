import sys
INF = 987654321

def dfs(now,visited):
    
    if visited == (1<<n)-1:
        if cost[now][0] :
            return cost[now][0]
        else :
            return INF
        
    ret = INF
    if (now,visited) in dp:
        return dp[(now,visited)]
    
    for next in range(1,n):
        
        if cost[now][next] == 0 or visited & (1<<next):
            continue
        
        total_cost = dfs(next,visited | (1<<next)) + cost[now][next]
        ret = min(ret,total_cost)
        
    dp[(now,visited)] = ret
    
    return ret
        

n = int(input())

cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = {}

    
print(dfs(0,1))