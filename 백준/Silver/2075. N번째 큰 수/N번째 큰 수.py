import heapq as h
import sys

n = int(input())


heap = []

for _ in range(n):
    for a in map(int,sys.stdin.readline().rstrip().split()):
        if len(heap) < n:
            h.heappush(heap,a)
        else:
            if a > heap[0]:
                h.heappop(heap)
                h.heappush(heap,a)
                
print(heap[0])