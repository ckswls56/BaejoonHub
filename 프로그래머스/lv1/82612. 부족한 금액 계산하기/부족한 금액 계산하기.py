def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer += price * (i+1)
    if money > answer :
        return 0
    return answer - money