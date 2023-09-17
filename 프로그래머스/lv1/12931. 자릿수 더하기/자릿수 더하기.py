def solution(n):
    answer = 0
    string = list(str(n))
    
    
    for s in string :
        answer += int(s)

    return answer