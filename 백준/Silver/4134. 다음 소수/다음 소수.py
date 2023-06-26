def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def findGreaterPrime(n):
    while(not isPrime(n)):
        n+=1
    return n

for i in range(int(input())) :
    n = int(input())
    print(findGreaterPrime(n))
    