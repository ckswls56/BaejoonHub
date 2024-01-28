def solution(participant, completion):
    answer = ''
    c_m = {}
    p_m = {}
    
    for c in completion :
        c_m[c] = c_m.get(c,0) + 1
    
    for p in participant :
        p_m[p] = p_m.get(p,0)+1
        
    for x,y in p_m.items():
        if c_m.get(x,x) != y:
            return x
        

            
    return answer