
h,w = map(int,input().split())

a = [list(input()) for _ in range(h)]

ans = [[-1]*w for _ in range(h)]

for i in range(h):
    for j in range(w-1,-1,-1):
        
        k = j
        flag = False
        while k >= 0 :
            if a[i][k] == 'c':
                flag = True
                break
            k-=1
        if flag:
            ans[i][j] = j-k
        
        
for a in ans:
    print(*a)