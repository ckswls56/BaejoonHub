def solution(s, skip, index):
    answer = []
    alpha = []
    for i in range(ord('a'),ord('z')+1):
        alpha.append(chr(i))
    
    for i in s:
        j = 0
        pos = alpha.index(i)
        
        while j <= index:
            if alpha[(pos+j) % 26] in skip :
                pos+=1
            else:
                j+=1
            
        answer.append(alpha[(pos+j-1) % 26])
        
    return ''.join(answer)
