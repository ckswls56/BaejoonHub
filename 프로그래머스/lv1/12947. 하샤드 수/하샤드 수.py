def solution(x):
    answer = True
    string = list(str(x))
    sum = 0
    for s in string :
        sum += int(s)
    if x % sum != 0 :
        answer = False
    return answer