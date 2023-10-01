def solution(n):
    prime = [0 for _ in range(n+1)]
    prime[0] = 1
    prime[1] = 1
    for i in range(2,n+1):
        if prime[i] : 
            continue
        for j in range(i*2,n+1,i):
            prime[j] = 1
    
    answer = prime.count(0)
    return answer