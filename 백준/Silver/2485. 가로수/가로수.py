def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a*b // gcd(a, b)


n = int(input())

arr = []
before = int(input())
for i in range(n-1):
    next = int(input())
    arr.append(next-before)
    before = next
g = arr[0]
for i in range(1, n-1):
    g = gcd(g, arr[i])

res = 0

for i in arr:
    res += i//g - 1

print(res)
