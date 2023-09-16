def solution(rank, attendance):
    for i in range(len(attendance)) :
        if not attendance[i]:
            rank[i] = 101
    sorted_list = sorted(rank)
    
    a = rank.index(sorted_list[0])
    b = rank.index(sorted_list[1])
    c = rank.index(sorted_list[2])

    answer = 10000*a+100*b+c
    
    return answer