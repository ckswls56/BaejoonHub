def make_prime(n):
    arr = [True]*(n+1)
    arr[0] = False
    arr[1] = False
    
    for i in range(2,n+1):
        if arr[i]:
            j=2
            while (i*j) <= n:
                arr[i*j] = False
                j+=1
                
    return arr

def solution(numbers):
    answer = 0
    num =[0 for i in range(10)]
    for n in numbers:
        num[int(n)] += 1
    
        
    prime = make_prime(9999999)
    cnt = 0
    for i in range(2,9999999):
        if prime[i]:
            temp = [0 for i in range(10)]
            ok = True
            for j in str(i):
                temp[int(j)] += 1
            
            for x,y in zip(num,temp):
                if x<y:
                    ok = False
                    break
                    
            if ok:
                answer+=1
                    
    return answer