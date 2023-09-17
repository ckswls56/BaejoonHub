def solution(n):
    answer = []
    string = list(str(n)[::-1])
    for s in string:
        answer.append(int(s))  # 문자열을 정수로 변환하여 추가
    return answer
