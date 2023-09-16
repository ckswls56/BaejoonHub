def solution(arr):
    # 입력 배열의 행(row)과 열(column) 길이 가져오기
    rows = len(arr)
    cols = len(arr[0])
    if rows > cols :
        big = rows
    else :
        big = cols

    # zeros 리스트 초기화 (행의 길이와 열의 길이가 다를 수 있으므로 따로 설정)
    zeros = [[0 for j in range(big)] for i in range(big)]

    # 입력 배열 값을 zeros 배열로 복사
    for i in range(rows):
        for j in range(cols):
            zeros[i][j] = arr[i][j]

    return zeros
