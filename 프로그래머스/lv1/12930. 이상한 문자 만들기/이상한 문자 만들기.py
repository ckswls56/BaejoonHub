def solution(s):
    answer = ''
    i = 0
    for l in s :
        if l.isalpha() :
            if i % 2 == 0:
                answer+=l.upper()
            else :
                answer+=l.lower()
            i+=1
        else :
            answer += l
            i = 0
        
        

    return answer