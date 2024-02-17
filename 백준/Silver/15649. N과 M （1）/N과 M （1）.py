from itertools import permutations

n,m = map(int,input().split())
l = [i for i in range(1,n+1)]
for c in permutations(l,m):
    for x in c:
        print(x,end=' ')
    print()