def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


arr = []

for i in range(1000001):
    arr.append(isPrime(i))

for i in range(int(input())):
    n = int(input())
    partion = 0
    for j in range(2, n//2+1):
        if arr[j] and arr[n-j]:
            partion += 1

    print(partion)