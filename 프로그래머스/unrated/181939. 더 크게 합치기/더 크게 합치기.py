def solution(a, b):
    c = int(str(a)+str(b))
    d = int(str(b)+str(a))
    if c>d :
        answer = c
    else :
        answer = d
    return answer