
def solution(n, results):
    
    answer = 0
    g = [[None]*(n)for _ in range(n)]
    
    for w,l in results:
        g[w-1][l-1] = True
        g[l-1][w-1] = False
        
    # i->j->k , i에서 k를 깔때 j를 거쳐서 갈 수 있는가
    # 일반적으로는 weight가 작은경우에만 update하면 되지만
    # 이문제에서는 연결된 것만 중요하다.
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if g[i][k] == None :
                    continue
                
                if g[i][k] == g[k][j]:
                    g[i][j] = g[i][k]
                    g[j][i] = not g[i][k]
    
    for i in range(n):
        if g[i].count(None) == 1 :
            answer+=1
    
    
    return answer