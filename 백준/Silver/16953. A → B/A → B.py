
def dfs(x,cnt):
    
    if x < a:
        return 1000000
    elif x == a:
        return cnt
    
    ret = 1000000
    
    if str(x)[-1] == '1':
        ret = min(dfs(int(str(x)[:-1]),cnt+1),ret)
    
    elif x%2 == 0 :
        ret = min(dfs(x//2,cnt+1),ret)
        
    return ret
    
    


a,b = map(int,input().split())

ret = dfs(b,1)
if ret == 1000000:
    print(-1)
else :
    print(ret)