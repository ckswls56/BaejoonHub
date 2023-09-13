def solution(myString):
    answer = []
    i=0
    for str in myString:
        if str == 'x':
            answer.append(i)
            i=-1
        i+=1
    answer.append(i)
    return answer