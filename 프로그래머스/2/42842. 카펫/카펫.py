def solution(brown, yellow):
    answer = []
    for i in range(3,brown):
        for j in range(3,i+1):
            #print(i,j)
            if (i*2)+j*2-4 == brown and (i-2)*(j-2) == yellow:
                return i,j
    return answer