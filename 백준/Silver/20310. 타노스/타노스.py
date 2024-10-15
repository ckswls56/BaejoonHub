
s=list(input())
z,o = s.count('0'),s.count('1')

n_s = '0' * (z//2) + '1' * (o//2)

print(n_s)