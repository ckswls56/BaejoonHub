n = int(input())

while n:
    n-=1
    answer = 0
    temp = 0
    for s in input():
        if s =='O':
            temp+=1
        else :
            temp = 0
        answer += temp
        
    print(answer)
