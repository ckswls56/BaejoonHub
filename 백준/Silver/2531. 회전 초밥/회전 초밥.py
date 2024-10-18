import sys

n,d,k,c = map(int,input().split())
arr = [0] * (n+k-1)
for i in range(n):
    arr[i] = int(sys.stdin.readline())

t_n = n+k-1    

for i in range(k-1):
    arr[n+i] = arr[i]
    
ans = 0

for i in range(n):
    s = set()
    for j in range(i,i+k):
        s.add(arr[j])
    temp = len(s)
    if c not in s:
        temp+=1
        
    ans = max(ans,temp)
    

print(ans)