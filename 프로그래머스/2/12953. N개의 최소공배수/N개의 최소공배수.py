def gcd (x,y):
    while y:
        x,y = y,x%y
    
    return x

def lcm (x,y):
    return x*y // gcd(x,y)
        

def solution(arr):
    answer = 1
    for a in arr:
        l = lcm(a,answer)
        if l > answer :
            answer = l
            
    
    return answer
