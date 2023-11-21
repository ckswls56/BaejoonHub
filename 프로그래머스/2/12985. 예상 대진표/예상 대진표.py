import math
def solution(n,a,b):
    answer = 0
    # 항상 b가 크게 유지
    if a>b :
        a,b = b,a
    
    
    while  a!=b:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer = answer + 1
    

    return answer