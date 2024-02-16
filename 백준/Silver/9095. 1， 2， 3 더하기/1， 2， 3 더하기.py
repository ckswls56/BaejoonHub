num = [1,2,3]

def dfs(x,n):
    if x>n:
        return 0
    elif x==n:
        return 1
    
    ret = 0

    for i in range(3):
        ret += dfs(x+num[i],n)
    
    return ret

    

t = int(input())
while t:
    n = int(input())
    print(dfs(0,n))
    t-=1
