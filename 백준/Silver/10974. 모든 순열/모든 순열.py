from itertools import permutations

n = int(input())

arr = list(range(1,n+1))

for combo in permutations(arr):
    print(*combo)
