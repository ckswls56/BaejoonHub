def solution(arr, n):
    answer= list()
    if len(arr) % 2 :
        for i in range(len(arr)):
            if i % 2 == 0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
    else :
        for i in range(len(arr)):
            if i % 2 == 1:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
            
    return answer