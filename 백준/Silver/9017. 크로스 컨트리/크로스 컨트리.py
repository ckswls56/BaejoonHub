from collections import Counter


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    c = Counter(arr)
    
    
    
    s_m = {}
    
    cnt = 1
    for a in arr :
        if c[a] == 6 :
            temp = s_m.get(a,[])
            temp.append(cnt)
            s_m[a] = temp
            cnt += 1
            
    
    res = []
    
    for k,v in s_m.items():
        res.append((k,v))
    
    res.sort(key=lambda x:(sum(x[1][:4]),x[1][4]))
    
    print(res[0][0])