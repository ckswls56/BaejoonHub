def solution(code):
    answer = ''
    mode = False
    for i in range(len(code)):
        if code[i] == '1':
            mode = not mode
        else :
            if mode and i % 2 :
                answer += code[i]
            if not mode and i % 2 == 0 :
                answer += code[i]
    if answer == '':
        answer = 'EMPTY'
    return answer