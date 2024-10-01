def is_valid(arr):
    # 모음과 자음의 개수를 세기 위한 함수
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = sum(1 for ch in arr if ch in vowels)
    consonant_count = len(arr) - vowel_count
    return vowel_count >= 1 and consonant_count >= 2

def sol(arr, i):
    if len(arr) == l:
        if is_valid(arr):  # 모음과 자음 개수 조건을 만족하는지 확인
            print("".join(arr))
        return
    
    for j in range(i, c):
        arr.append(possible[j])
        sol(arr, j + 1)  # 다음 인덱스를 `j+1`로 넘겨야 중복 방지
        arr.pop()

l, c = map(int, input().split())
possible = input().split()

possible.sort()  # 사전순으로 정렬
sol([], 0)
