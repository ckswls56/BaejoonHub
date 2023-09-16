def solution(arr):
    square = [2**i for i in range(11)]
    while len(arr) not in square :
        arr.append(0)
    return arr