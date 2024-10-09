import sys
import heapq as h
n = int(input())
arr = []

for _ in range(n):
    s,e = map(int, sys.stdin.readline().rstrip().split())
    arr.append((s,e))
    
arr.sort()

ans = 1

heap = [0]

for s,e in arr:
    
    if s >= heap[0]:
        h.heappop(heap)
    else :
        ans += 1
    h.heappush(heap,e)
    
print(ans)