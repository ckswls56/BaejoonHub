def solution(str_list):
    answer = []
    idx = 0
    for s in str_list :
        if s == 'l':
            answer = str_list[:idx]
            break
        elif s == 'r' :
            answer = str_list[idx+1:]
            break
        idx +=1
        
    return answer