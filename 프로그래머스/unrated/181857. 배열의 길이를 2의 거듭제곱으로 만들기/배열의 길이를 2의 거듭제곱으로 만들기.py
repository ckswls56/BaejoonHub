def solution(arr):
    answer = []
    square = [2**i for i in range(11)]
    if len(arr) in square :
        return arr
    else :
        while len(arr) not in square :
            arr.append(0)

    return arr