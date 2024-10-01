from itertools import permutations

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
res = []
for combo in set(permutations(arr,m)):
    res.append(combo)
    
res.sort()

for r in res:
    print(*r)