import sys
input = sys.stdin.readline

def is_possible(s):
    can_use = b
    time = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] == s:
                continue
            else :
                if ground[i][j]>s:
                    can_use += ground[i][j]-s
                    time += (ground[i][j]-s)*2
                else :
                    can_use -= s-ground[i][j]
                    time += s-ground[i][j]
    
    if can_use >= 0:
        return time
    else :
        return -1


n,m,b = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(n)]
mins = 256
maxs = 0

for i in range(n):
    for j in range(m):
        mins = min(mins,ground[i][j])
        maxs = max(maxs,ground[i][j])

possible = []
for s in range(mins,maxs+1):
    temp = is_possible(s)
    if temp != -1:
        possible.append((temp,s))

possible.sort(key = lambda x : (x[0],-x[1]))

print(*possible[0])