strings = []  # 문자열들을 저장할 리스트
strings_len = list()
for _ in range(5):  # 5줄에 대해 반복
    string = input()  # 한 줄을 입력받음
    characters = [ch for ch in string]  # 문자열을 문자(character) 단위로 쪼개어 리스트에 저장
    strings.append(characters)  # 문자(character) 리스트를 문자열 리스트에 추가

for i in range(15):
    for j in range(5):
        if(len(strings[j]) <= i):
            continue
        if(strings[j][i]):
            print(strings[j][i], end="")
