import math

def convert(n, k):
    res = ''
    while n > 0:
        n, m = divmod(n, k)
        res += str(m)
    
    return res[::-1]

def isPrime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution(n, k):
    answer = 0
    convert_list = list(filter(None, convert(n, k).split('0')))
    
    for c in convert_list:
        if isPrime(int(c)):
            answer += 1
    
    return answer
