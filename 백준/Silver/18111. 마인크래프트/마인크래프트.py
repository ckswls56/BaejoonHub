import sys
input = sys.stdin.readline

def is_possible(s):
    can_use = b
    time = 0
    for h,v in height.items():
        if h != s:
            if h>s:
                can_use += (h-s)*v
                time += (h-s)*2*v
            else :
                can_use -= (s-h)*v
                time += (s-h)*v
    
    if can_use >= 0:
        return time
    else :
        return -1


n,m,b = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(n)]
height = {}
for i in range(n):
    for j in range(m):
        if ground[i][j] in height:
            height[ground[i][j]] += 1
        else :
            height[ground[i][j]] = 1

possible = []
for s in range(0,257):
    temp = is_possible(s)
    if temp != -1:
        possible.append((temp,s))

possible.sort(key = lambda x : (x[0],-x[1]))

print(*possible[0])