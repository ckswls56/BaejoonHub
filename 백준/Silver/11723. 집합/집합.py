import sys
m = int(input())

s = 0

for _ in range(m):
    strings = sys.stdin.readline().rstrip()
    
    try :
        c,v = strings.split()
        v = int(v)
    
        if c == 'add':
            s |= (1<<v)
        elif c == 'remove':
            s &= ~(1<<v)
        elif c == 'check':
            print(1 if s & (1<<v) else 0)
        elif c == 'toggle':
            s ^= (1<<v)
    except:
        if strings == 'all':
            s = (1<<21)-1
        elif strings == 'empty':
            s = 0