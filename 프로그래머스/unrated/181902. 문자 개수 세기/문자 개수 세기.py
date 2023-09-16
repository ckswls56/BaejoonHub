import string
def solution(my_string):
    answer = []
    arr=list(string.ascii_uppercase + string.ascii_lowercase)
    for i in arr :
        answer.append(my_string.count(i))
    return answer