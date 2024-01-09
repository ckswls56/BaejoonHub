def solution(elements):
    s = set()
    
    for i in range(len(elements)):
        
        for j in range(0,len(elements)):
            
            overflow = len(elements)-(j+i+1)
            seq = sum(elements[j:j+i+1])
            
            if overflow<0:
                seq += sum(elements[0:-overflow])
                
            s.add(seq)
            
            
    return len(s)