from collections import deque

n,m,r = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

k = min(n,m)//2

for i in range(k):
    
    new_arr = deque()
    
    new_arr.extend(arr[i][i:m-i])
    new_arr.extend([row[m-i-1] for row in arr[i+1:n-i-1]])
    new_arr.extend(arr[n-i-1][i:m-i][::-1])
    new_arr.extend([row[i] for row in arr[i+1:n-i-1]][::-1])
    
    new_arr.rotate(-r)
    
    for j in range(i,m-i):
        arr[i][j] = new_arr.popleft()
    for j in range(i+1,n-i-1):
        arr[j][m-i-1] = new_arr.popleft()
    for j in range(m-i-1,i-1,-1):
        arr[n-i-1][j] = new_arr.popleft()
    for j in range(n-i-2,i,-1):
        arr[j][i] = new_arr.popleft()
        

for line in arr:
    print(*line)