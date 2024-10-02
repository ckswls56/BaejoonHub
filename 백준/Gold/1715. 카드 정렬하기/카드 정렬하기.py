import heapq as h
import sys

n = int(input())
arr = []
for _ in range(n):
    h.heappush(arr,int(sys.stdin.readline().rstrip()))
    

ans = 0

while len(arr) > 1 :
    next = h.heappop(arr) + h.heappop(arr)
    ans += next
    h.heappush(arr,next)
    
print(ans)