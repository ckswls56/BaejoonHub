def solution(n, m, section):
    answer = 0
    before = 0
    for i in range(1,len(section)):
        if section[i] - section[before] < m :
            continue
        else :
            before = i
            answer += 1
        
    return answer+1