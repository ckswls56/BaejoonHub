import math
def solution(n):
    answer = -1
    for i in range(1,int(math.sqrt(50000000000000))):
        if i ** 2 == n :
            answer =(i+1)**2
            break
    return answer