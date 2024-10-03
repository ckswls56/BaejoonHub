def get_diff(a,b,x1,x2):
    cnt = 0
    for i in range(min(len(a),len(b))):
        if a[i] != b[i] and x1<=i<x2:
            cnt += 1
            
    return cnt


a,b = input().split()

diff = len(b)-len(a)

if diff == 0:
    cnt = 0
    for i in range(min(len(a),len(b))):
        if a[i] != b[i]:
            cnt += 1
    print(cnt)
else:
    res = 50
    for i in range(diff+1):
        t1,t2 = 'a'*i,'a'*(diff-i)
        
     
        res = min(res,get_diff(t1+a+t2,b,i,len(a)+i))
        
    print(res)
    
    