def solution(k, tangerine):
    count=[0]*10000001
    
    for t in tangerine:
        count[t] += 1
    
    
    count.sort(reverse = True)
    answer = 1

    for c in count :
        if k - c > 0 :
            answer += 1
            k-=c
        else :
            break
        

    return answer