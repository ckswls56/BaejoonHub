from itertools import *
def solution(number):
    answer = 0
    comb = list(combinations(number,3))
    for c in comb :
        if c[0]+c[1]+c[2] == 0 :
            answer+=1
    return answer