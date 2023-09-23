def solution(a, b, n):
    answer = 0
    while n >= a :
        answer += b * (n//a)
        n = n- ((n//a)*a) + n//a * b
    return answer