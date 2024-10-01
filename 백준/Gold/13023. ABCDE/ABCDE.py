

def sol(sets,s):
    
    if len(sets) == 5:
        return True
     
    for a in g[s]:
        if a not in sets:
            sets.add(a)
            if sol(sets,a):
                return True
            sets.remove(a)
    
    return False
n,m = map(int,input().split())

g = [[]for _ in range(n)]

for _ in range(m):
    s,e = map(int,input().split())
    g[s].append(e)
    g[e].append(s)


for i in range(n):
    if sol(set({i}),i):
        print(1)
        exit(0)

print(0)