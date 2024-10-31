import sys
import heapq as h
input = sys.stdin.readline
INF = 987654321

n,m = map(int,input().rstrip().split())
d = [INF] * (n+1)
g = [[] for _ in range(n+1)]


for _ in range(m):
    s,e,c = map(int,input().rstrip().split())
    g[s].append((e,c))
    g[e].append((s,c))
    

# dijkstra

heap = []
heap.append((0,1))
d[1] = 0

while heap:
    distance, current = h.heappop(heap)
    
    if d[current] < distance:
        continue

    
    for next,next_distance in g[current]:
        total_distance = distance + next_distance
        if d[next] > total_distance:
            h.heappush(heap,(total_distance,next))
            d[next] = total_distance
    
print(d[n])