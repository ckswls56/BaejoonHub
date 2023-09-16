def solution(arr):
    before = arr[:]
    answer = 0
    idx = 0
    while True :
        for i in range(len(arr)) :
            if arr[i] >= 50 and arr[i] % 2 == 0 :
                arr[i] //= 2
            elif arr[i] <= 50 and arr[i] % 2 :
                arr[i] = arr[i] *2 + 1
            
        if before == arr :
            return answer
        before = arr[:]
        answer += 1