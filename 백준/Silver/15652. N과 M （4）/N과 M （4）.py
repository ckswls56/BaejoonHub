from itertools import combinations_with_replacement

n,m = map(int,input().split())
l = [i for i in range(1,n+1)]
for c in combinations_with_replacement(l,m):
    for x in c:
        print(x,end=' ')
    print()