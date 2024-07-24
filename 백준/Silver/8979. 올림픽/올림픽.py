n,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:(-x[1],-x[2],-x[3]))
res = 1
temp = 0
b_g,b_s,b_b = 0,0,0

for c,g,s,b in arr:
    if b_g == g and b_s == s and b_b == b:
        temp+=1
        continue
    else:
        res += temp
        temp=1
    
    if c == k:
        print(res-1)
        break
    
    