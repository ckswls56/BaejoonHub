def check_include(string):
    # 문자열에 모음이 하나라도 있는지 확인
    return any(s in 'aeiou' for s in string)

def check_continuous(string):
    cnt = 1
    is_vowel = check_include(string[0])

    for i in range(1, len(string)):
        if check_include(string[i]) == is_vowel:  # 이전 문자와 같은 종류 (모음/자음)인가?
            cnt += 1
        else:
            cnt = 1  # 연속성이 깨졌으므로 카운트 초기화
            is_vowel = not is_vowel  # 종류 변경

        if cnt >= 3:  # 모음이나 자음이 3개 연속으로 온 경우
            return False

    return True

def check_same(string):
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            if string[i] not in ('e', 'o'):  # ee, oo는 허용
                return False
    return True

string = input()

while string != 'end':
    # 세 조건을 모두 만족하는지 확인
    if check_include(string) and check_continuous(string) and check_same(string):
        print('<', string, '> is acceptable.', sep='')
    else:
        print('<', string, '> is not acceptable.', sep='')
    
    string = input()
