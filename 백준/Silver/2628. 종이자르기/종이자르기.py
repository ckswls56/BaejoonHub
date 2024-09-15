x,y = map(int,input().split())

n = int(input())

garo,sero = [(0,x)],[(0,y)]


for _ in range(n):
    c,x = map(int,input().split())
    
    if c == 1:
        for i in range(len(garo)):
            
            b,t = garo[i]
            
            if b<=x<=t:
                garo.pop(i)
                
                garo.append((b,x))
                garo.append((x,t))
    else:
        for i in range(len(sero)):
            
            b,t = sero[i]
            
            if b<=x<=t:
                sero.pop(i)
                
                sero.append((b,x))
                sero.append((x,t))


garo_maxs = max(garo,key=lambda x :(x[1]-x[0]))
sero_maxs = max(sero,key=lambda x :(x[1]-x[0]))

print((garo_maxs[1]-garo_maxs[0]) * (sero_maxs[1]-sero_maxs[0]))