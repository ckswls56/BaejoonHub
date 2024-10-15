from bisect import bisect_left,bisect_right
s=list(input())

z,o = s.count('0')//2,s.count('1')//2

remove = []

while o :
    o-=1
    r = s.index('1')
    s[r] = ''
r_s = list(reversed(s))
while z:
    z-=1
    r = r_s.index('0')
    r_s[r] = ''
    r = len(s)-1- r
    s[r] = ''


n_s = list(filter(lambda x : x!='',s))

print("".join(n_s))