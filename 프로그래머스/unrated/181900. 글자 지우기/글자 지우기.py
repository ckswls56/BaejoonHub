def solution(my_string, indices):
    answer = ''
    l = list(my_string)
    for i in indices:
        l[i] = '!'
    for i in l :
        if i != '!':
            answer += i
    return answer