def solution(arr1, arr2):
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else :
        sum1 = 0
        sum2 = 0
        for i in range(len(arr1)):
            sum1+=arr1[i]
            sum2+=arr2[i]
        if sum1>sum2:
            answer = 1
        elif sum1<sum2:
            answer = -1
        else :
            answer = 0
            
    return answer