def solution(s):
    
    p = s.upper().count('P')
    y = s.upper().count('Y')
    
    if p == y :
        answer = True
    else :
        answer = False

    return answer