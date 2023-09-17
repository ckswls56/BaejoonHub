def solution(n):
    answer = 0
    temp = ''

    while n > 0 :
        r = n % 3
        temp = str(r) + temp
        n = n//3
        
    temp = temp[::-1]
    
    for i in range(1,len(temp)+1):
        answer += int(temp[-i])*3**(i-1)
    return answer