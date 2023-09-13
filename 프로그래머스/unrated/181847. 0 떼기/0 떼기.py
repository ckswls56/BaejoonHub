def solution(n_str):
    answer = ''
    flag = False
    for s in n_str :
        if flag or s != '0':
            answer += s
            flag = True
            
    return answer