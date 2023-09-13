def solution(myString):
    answer = ''
    for s in myString :
        if s == 'a'or s == 'A':
            answer += 'A'
        else :
            answer += s.lower()
            
    return answer