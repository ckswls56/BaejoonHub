def solution(s):
    answer = 0
    i = 0
    x = None
    
    while i < len(s):
        if x == None:
            x = s[i]
            answer+=1
            x_cnt = 1
            others_cnt = 0
        else :
            if s[i] == x :
                x_cnt += 1
            else :
                others_cnt += 1
            
            if x_cnt == others_cnt :
                x = None
        i+=1
        
        
    return answer