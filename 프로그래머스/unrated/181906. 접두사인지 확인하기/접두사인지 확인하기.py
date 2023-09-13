def solution(my_string, is_prefix):
    if len(my_string)<len(is_prefix):
        answer = 0
    else :
        answer = 1
        for i in range(len(is_prefix)):
            if my_string[i] != is_prefix[i]:
                answer = 0
                break
    return answer