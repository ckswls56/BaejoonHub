def solution(my_string, m, c):
    answer = ''
    strArr = []
    times = len(my_string) // m
    sum = 0
    for i in range(times):
        strArr.append(my_string[sum:sum+m])
        sum += m
    
    for i in range(len(strArr)):
        answer += strArr[i][c-1]
        
    return answer