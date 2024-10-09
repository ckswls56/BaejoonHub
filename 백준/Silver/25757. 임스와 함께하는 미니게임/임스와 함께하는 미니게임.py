import sys
n,game = input().split()
n = int(n)

s = set()

if game == 'Y':
    need = 1
elif game == 'F':
    need = 2
else :
    need = 3

ans = 0
before = 0
cnt = 0
for _ in range(n):
    p = sys.stdin.readline()
    s.add(p)
    
    if len(s) != before:
        cnt += 1
        before = len(s)
        
    if cnt == need:
        ans += 1
        cnt = 0

    
print(ans)