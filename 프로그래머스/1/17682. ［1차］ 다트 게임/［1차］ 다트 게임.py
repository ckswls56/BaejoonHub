def solution(dartResult):
    num = []
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdecimal():
            # 만약 현재 문자가 숫자라면, 연속된 숫자들을 하나의 숫자로 처리
            if i + 1 < len(dartResult) and dartResult[i+1].isdecimal():
                num.append(int(dartResult[i:i+2]))
                i += 1  # 두 자리 숫자 처리를 위해 인덱스 1 증가
            else:
                num.append(int(dartResult[i]))
        elif dartResult[i] == 'D':
            num[-1] = num[-1] ** 2
        elif dartResult[i] == 'T':
            num[-1] = num[-1] ** 3
        elif dartResult[i] == '#':
            num[-1] = -num[-1]
        elif dartResult[i] == '*':
            if len(num) > 1:
                num[-1] *= 2
                num[-2] *= 2
            else:
                num[-1] *= 2
        i += 1  # 다음 문자 처리를 위해 인덱스 1 증가

    return sum(num)