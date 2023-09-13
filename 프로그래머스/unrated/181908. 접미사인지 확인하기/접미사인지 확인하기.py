def solution(my_string, is_suffix):
    if len(is_suffix)>len(my_string):
        answer = 0
    else :
        answer = 1
        for i in range(1,len(is_suffix)+1):
            if my_string[-i] != is_suffix[-i] :
                answer = 0
                break;
    return answer