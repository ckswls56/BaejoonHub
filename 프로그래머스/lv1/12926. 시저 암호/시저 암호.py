import string
def solution(s, n):
    answer = ''
    
    lower_list = list(string.ascii_lowercase)
    upper_list = list(string.ascii_uppercase)
    for i in s:
        if i != ' ':
            if i in lower_list:
                idx = lower_list.index(i)
                answer+= lower_list[(idx+n) % 26]
            else :
                idx = upper_list.index(i)
                answer+= upper_list[(idx+n) % 26]
        else :
            answer += ' '
    return answer