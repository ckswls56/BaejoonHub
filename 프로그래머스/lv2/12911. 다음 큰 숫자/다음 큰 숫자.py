def check(a,b):
    return bin(a).count('1') == bin(b).count('1')

def solution(n):
    for i in range(n+1,1000001):
        if check(n,i):    
            return i