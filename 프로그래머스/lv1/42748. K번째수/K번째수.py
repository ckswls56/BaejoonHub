def solution(array, commands):
    answer = []
    for c in commands :
        s,e,i = c
        temp = array[s-1:e]
        temp.sort()
        answer.append(temp[i-1])
    return answer