def solution(n, arr1, arr2):
    answer = []
    str1 = []
    str2 = []
    for i in arr1 :
        str1.append(bin(i)[2:].zfill(len(arr1)))
    for i in arr2 :
        str2.append(bin(i)[2:].zfill(len(arr1)))

    for i in range(len(str1)):
        temp = ''
        for j in range(len(str1[i])):
            if str1[i][j] == '1' or str2[i][j] == '1':
                temp +='#'
            else :
                temp +=' '
        answer.append(temp)
    return answer