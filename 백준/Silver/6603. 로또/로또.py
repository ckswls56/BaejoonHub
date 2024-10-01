from itertools import combinations

arr = list(map(int,input().split()))

while len(arr) > 1:
    for combo in list(combinations(arr[1:],6)):
        print(*combo)
    print()
    arr = list(map(int,input().split()))