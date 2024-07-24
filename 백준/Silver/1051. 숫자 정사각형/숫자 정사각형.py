n,m = map(int,input().split())
inputs = [input() for _ in range(n)]
rectangle = [list(row) for row in inputs]

max_size = min(n,m)
ans = 1

for k in range(2,max_size+1):
    for i in range(n-k+1):
        for j in range(m-k+1):
            if rectangle[i][j]==rectangle[i+k-1][j]==rectangle[i][j+k-1]==rectangle[i+k-1][j+k-1]:
                ans = k
                break
            
            
print(ans**2)