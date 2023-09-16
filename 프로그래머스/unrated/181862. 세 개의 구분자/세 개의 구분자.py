def solution(myStr):
    str = list(myStr)
    answer = ''
    for s in str :
        if s == 'a' or s == 'b' or s == 'c' :
            answer += '!'
        else :
            answer += s
        
    answer = list(filter(None,answer.split('!')))
    if not answer :
        answer.append('EMPTY')
    return answer