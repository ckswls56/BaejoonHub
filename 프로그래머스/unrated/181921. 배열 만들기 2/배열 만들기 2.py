def solution(l, r):
    answer = []
    for i in range(l,r+1):
        flag = True
        for j in range(1,10):
            if str(j) in str(i) and j != 5:
                flag = False
                break
        if flag :
            answer.append(i)
    if not answer :
        answer.append(-1)
    return answer