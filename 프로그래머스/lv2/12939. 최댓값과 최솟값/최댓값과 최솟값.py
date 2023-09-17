def solution(s):
    string = s.split()
    int_array = [int(x) for x in string]
    answer = str(min(int_array)) + " " + str(max(int_array))

    return answer