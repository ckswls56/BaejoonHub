def solution(n):
    string = sorted(str(n),reverse = True)
    answer = int(''.join(string))
    return answer