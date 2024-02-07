def solution(n, s):
    a = s // n
    b = s % n
    if a < 1:
        return [-1]
    
    
    answer = [a]*n
    
    for i in range(b):
        answer[i]+=1
    
    answer.sort()
            
    ##s를 n으로 나누고 나머지들을 더해준다!
    
    return answer