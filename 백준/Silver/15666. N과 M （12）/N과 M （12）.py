
from itertools import combinations_with_replacement

n,m = map(int,input().split())
arr = list(map(int,input().split()))

res = []
arr.sort()

for combo in set(combinations_with_replacement(arr,m)):
    res.append(combo)
    
res.sort()

for r in res:
    print(*r)