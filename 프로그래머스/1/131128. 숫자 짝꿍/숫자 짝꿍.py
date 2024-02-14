def only_zero(string):
    
    for st in string:
        for s in st:
            if s != '0':
                return False
    return True
        

def solution(X, Y):
    answer = []
   
    m1 = {}
    m2 = {}
    for x in X:
       
        m1[x] = m1.get(x,0) +1
    for y in Y:
     
        m2[y] = m2.get(y,0) +1
        
    
    
    set1 = set(list(m1.keys()))
    
    set2 = set(list(m2.keys()))
    res_set = set1.intersection(set2)
    
    if len(res_set) == 0:
        return "-1"
    else :
        for r in res_set:
            if m1[r]<m2[r]:
                
                answer.append(str(r)*m1[r])
            else :
                answer.append(str(r)*m2[r])
            
        answer.sort(reverse=True)
    
    if len(answer) == 1 and only_zero(answer):
        return "0"
    else:
        return ''.join(answer)
    
    