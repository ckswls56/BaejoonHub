import sys

parent = [i for i in range(1000001)]

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


input = sys.stdin.readline
n, m = list(map(int, input().split()))


for _ in range(m):
    op,a,b = list(map(int, input().split()))
    if op == 0 :
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")