
from itertools import combinations

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
for combo in combinations(arr,m):
    print(*combo)