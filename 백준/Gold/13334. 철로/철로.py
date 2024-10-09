import sys
import heapq as h

input = sys.stdin.readline
n = int(input())

arr = []

for _ in range(n):
    s,e = map(int, sys.stdin.readline().rstrip().split())
    s,e = min(s,e),max(s,e)
    arr.append((s,e))
    
d = int(input())

    
arr.sort(key = lambda x:x[1])

heap = []
ans = 0

for s,e in arr:
    
    h.heappush(heap,s)
    # 시작점
    line_start = e-d
    # 시작점 보다 작은 값들 제거
    while heap and heap[0] < line_start :
        h.heappop(heap)
    ans = max(ans,len(heap))
    
print(ans)     