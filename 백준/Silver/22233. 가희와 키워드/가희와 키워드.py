import sys
n,m = map(int,input().split())
d = set()
for _ in range(n):
    d.add(sys.stdin.readline().rstrip())
    
for _ in range(m):
    arr = set(sys.stdin.readline().rstrip().split(','))
    d-=arr
    
    print(len(d))