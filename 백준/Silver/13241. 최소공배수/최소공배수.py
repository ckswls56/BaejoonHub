def gcd(a, b):
    while(b > 0):
        tmp = a
        a = b
        b = tmp % b
    return a


def lcm(a, b):
    return a*b // gcd(a, b)


a, b = map(int, input().split())

print(lcm(a, b))
