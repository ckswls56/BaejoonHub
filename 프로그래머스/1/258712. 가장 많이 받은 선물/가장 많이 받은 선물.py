from itertools import combinations
def solution(friends, gifts):
    answer = 0
    m = {}
    point = {}
    res = {}
    for f in friends:
        m[f] = {}
        point[f] = 0
        res[f] = 0
    
    for g in gifts :
        a,b = g.split()[0],g.split()[1]
        m[a][b] = m[a].get(b,0)+1
        point[a] += 1
        point[b] -= 1
    
    
    for a,b in combinations(friends,2):
        
        if m[a].get(b,0) > m[b].get(a,0) :
            
            res[a] += 1
        elif m[a].get(b,0) < m[b].get(a,0) :
            
            res[b] += 1
        else :
            if point[a] > point[b] :
                res[a]+=1
            elif point[a] < point[b] :
                res[b]+=1
            
    answer = max(res.values())
    return answer