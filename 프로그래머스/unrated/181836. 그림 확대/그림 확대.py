def solution(picture, k):
    answer = []
    for str in picture :
        pixel = list(str)
        temp = ''
        for p in pixel :
            temp += p * k
        for i in range(k):
            answer.append(temp)
        
    return answer