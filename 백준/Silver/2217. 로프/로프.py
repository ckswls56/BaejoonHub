import sys

n = int(input())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
    
arr.sort()

ans = 0

for i in range(n):
    ans = max(arr[i]*(n-i),ans)
    
print(ans)