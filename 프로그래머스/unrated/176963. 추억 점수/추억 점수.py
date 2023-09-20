def solution(name, yearning, photo):
    answer = []
    for arr in photo:
        sum = 0
        print(arr)
        for i in arr :
            try:
                idx = name.index(i)
                sum+=yearning[idx]
            except :
                pass
                
        answer.append(sum)
    return answer