def solution(arr, queries):
    answer = []
    for q in queries :
        temp = arr[q[0]]
        arr[q[0]] = arr[q[1]]
        arr[q[1]] = temp
    answer = arr
    return answer