
idx = 0

def sol(c):
    global idx
    
    if(c*2 < 2**k and tree[c*2] == 0):
        sol(c*2)
    
    tree[c] = a[idx]
    idx+=1
        
    if (c*2+1 < 2**k and tree[c*2+1] == 0):
        sol(c*2+1)
    

    return

k = int(input())

a = list(map(int,input().split()))

tree = [0] * (2**k)


current = 1

sol(1)

j = 1
for i in range(1,2**k):
    
    print(tree[i],end=" ")
    
    if (i+1) % j == 0:
        print()
        j*=2    