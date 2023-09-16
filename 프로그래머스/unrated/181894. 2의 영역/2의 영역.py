def solution(arr):
    answer = []
    lIdx = -1
    rIdx = -1
    for i in range(len(arr)):
        if arr[i] == 2 :
            lIdx = i
            break
    
    for i in range(len(arr)-1,0,-1):
        if arr[i] == 2 :
            rIdx = i
            break
        
    if lIdx == -1 :
        answer.append(-1)
    elif lIdx == rIdx :
        answer.append(2)
    else :
        answer = arr[lIdx:rIdx+1]
    return answer