import sys
from collections import Counter

n = int(input())

arr = [sys.stdin.readline().rstrip() for _ in range(n)]

c = Counter(arr)
top = c.most_common(1)[0][1]

res = []

for c,v in c.items():
    if v == top:
        res.append(c)
        

res.sort()

print(res[0])