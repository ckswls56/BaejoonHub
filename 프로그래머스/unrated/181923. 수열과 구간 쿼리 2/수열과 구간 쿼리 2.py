def solution(arr, queries):
    answer = []
    for q in queries:
        min = 1000001
        for i in range(q[0],q[1]+1):
            if arr[i] > q[2] and arr[i] < min :
                min = arr[i]
        if min == 1000001 :
            answer.append(-1)
        else :
            answer.append(min)
            
    return answer