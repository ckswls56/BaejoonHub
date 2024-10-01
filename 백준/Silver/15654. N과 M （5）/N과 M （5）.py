from itertools import permutations

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
for combo in permutations(arr,m):
    print(*combo)