def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer+= str(i) * int(food[i]//2)
    temp = answer [::-1]
    answer+='0'
    answer+= temp

    return answer