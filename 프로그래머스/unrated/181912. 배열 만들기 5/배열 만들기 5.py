def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs :
        temp = int(str[s:s+l])
        if temp > k :
            answer.append(temp)
    return answer