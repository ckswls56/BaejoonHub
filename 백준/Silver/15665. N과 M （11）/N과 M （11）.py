from itertools import product

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

for combo in sorted(list(set(product(arr,repeat=m)))):
    print(*combo)