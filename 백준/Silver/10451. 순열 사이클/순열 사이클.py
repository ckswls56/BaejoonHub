def make_root(n):
    root = [i for i in range(n+1)]
    return root

def find(x,root):
    if x==root[x]:
        return x
    else :
        root[x] = find(root[x],root)
        return root[x]
    
def union(x,y,root):
    x = find(x,root)
    y = find(y,root)

    if x<y:
        root[y] = x
    else:
        root[x] = y


t = int(input())

while t:
    t-=1
    n = int(input())
    answer = 0    
    arr = list(map(int,input().split()))
    sort = sorted(arr)
    root = make_root(n)
    
    
    for x,y in zip(arr,sort):
        
        if find(x,root) == find(y,root):
            answer += 1
        else :
            union(x,y,root)
    
    print(answer)