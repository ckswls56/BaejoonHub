def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a*b // gcd(a, b)


a, b = map(int, input().split())
c, d = map(int, input().split())

l = lcm(b, d)
u = a*(l//b)+c*(l//d)
g = gcd(u, l)
if g == 1:
    print(u, l)
else:
    print(u//g, l//g)
