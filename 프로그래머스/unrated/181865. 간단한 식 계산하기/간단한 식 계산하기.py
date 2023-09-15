def solution(binomial):
    answer = 0
    strArr = binomial.split()
    if strArr[1] == '+' :
        answer = int(strArr[0]) + int(strArr[2])
    elif strArr[1] == '-' :
        answer = int(strArr[0]) - int(strArr[2])
    else :
        answer = int(strArr[0]) * int(strArr[2])
    return answer