def divCnt(n):
    div=[]
    for i in range(1,int(n**(0.5))+1):
        if n % i == 0:
            div.append(i)
            if i != n//i :
                div.append(n//i)
    return len(div)

def solution(number, limit, power):
    div = []
    for i in range(1,number+1):
        div.append(divCnt(i))
    
    for i in range(len(div)):
        if div[i] > limit:
            div[i] = power
    
    return sum(div)