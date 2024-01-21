def solution(arr1, arr2):
    answer = []
    
    # 행렬 arr1의 행의 개수
    rows_arr1 = len(arr1)
    # 행렬 arr1의 열의 개수
    cols_arr1 = len(arr1[0])
    # 행렬 arr2의 열의 개수
    cols_arr2 = len(arr2[0])

    for i in range(rows_arr1):
        row = []
        for j in range(cols_arr2):
            # 각 원소를 계산할 때, zip 함수를 사용하여 효율적으로 계산
            temp = sum(a * b for a, b in zip(arr1[i], (row[j] for row in arr2)))
            row.append(temp)
        answer.append(row)

    return answer
