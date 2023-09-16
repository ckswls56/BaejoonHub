def solution(q, r, code):
    answer = ''
    str = list(code)
    for i in range(len(str)) :
        if i % q == r :
            answer += str[i]
    return answer