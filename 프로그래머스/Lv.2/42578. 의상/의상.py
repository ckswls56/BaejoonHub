def solution(clothes):
    d = dict()
    answer = 1
    
    for c in clothes :
        if c[1] in d:
            temp = d[c[1]]
        else :
            temp = []
        temp.append(c[0])
        d[c[1]]=temp
    
    for i in d.values():
        answer *= len(i)+1
    
    return answer-1