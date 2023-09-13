def solution(my_string, alp):
    answer = ''
    for s in my_string :
        if s in alp:
            answer+=s.upper()
        else :
            answer+=s
    return answer