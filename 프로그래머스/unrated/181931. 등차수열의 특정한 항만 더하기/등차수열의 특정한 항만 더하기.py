def solution(a, d, included):
    answer = 0
    sum = a
    for i in range(len(included)):
        if included[i] :
            answer+= sum
        sum += d
    return answer