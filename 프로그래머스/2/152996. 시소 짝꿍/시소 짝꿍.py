from math import comb

def solution(weights):
    m = {}
    
    for w in weights:
        m[w] = m.get(w,0) + 1
    
    l = m.items()
    answer =0
    same = 0
    for k,v in m.items():
        same += comb(v,2)
        
        for another_k,another_v in l :
            if k != another_k:
                for i in (2,3,4):
                    for j in (2,3,4):
                        if k*i == another_k *j:
                            answer += v*another_v
            
    
    return answer//2 + same