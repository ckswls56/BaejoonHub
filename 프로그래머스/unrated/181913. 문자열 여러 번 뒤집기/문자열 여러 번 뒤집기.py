def solution(my_string, queries):
    for q in queries :
        my_string = my_string[:q[0]] + my_string[q[0]:q[1]+1][::-1] + my_string[q[1]+1:]
    return my_string