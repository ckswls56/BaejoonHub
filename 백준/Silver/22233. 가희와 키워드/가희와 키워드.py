import sys
n,m = map(int,input().split())
d = set()
for _ in range(n):
    d.add(sys.stdin.readline().rstrip())
    
for _ in range(m):
    arr = list(sys.stdin.readline().rstrip().split(','))
    for a in arr:
        if a in d:
            d.remove(a)
    
    print(len(d))