from itertools import combinations

visit = [False]*101

def make_tree(wires,n):
    graph = [[False]*(n+1) for _ in range(n+1)]
    for s,e in wires:
        graph[s][e] = True
        graph[e][s] = True
    
    return graph

def dfs(graph,start):
    res = 0
    visit[start] = True
    
    for i in range(len(graph[start])):
        if graph[start][i] and not visit[i]:
            res += dfs(graph,i)
            res += 1
            
    return res

def solution(n, wires):
    answer = -1
    res = 100
    
    for wire in combinations(wires, len(wires)-1):
        graph = make_tree(wire, n)
        a=dfs(graph,wire[0][0])+1
        b = n - a
        res=min(res,abs(a-b))
        
        # visit 리스트 초기화
        for i in range(101):
            visit[i] = False
        
    return res
