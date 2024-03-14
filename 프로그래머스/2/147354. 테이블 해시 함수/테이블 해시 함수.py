def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x : (x[col-1],-x[0]))
    s=[]
    
    for i in range(row_begin-1,row_end):
        temp = 0
        for d in data[i]:
            temp += d % (i+1)
        s.append(temp)
    
    answer = s[0]
    for x in s[1:]:
        answer = answer ^ x
        
            
    
    return answer