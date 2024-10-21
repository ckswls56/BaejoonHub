import sys
import heapq as h

def dijkstra(start):
    heap = []
    h.heappush(heap, (0, start))  # heapq.heappush 사용
    d[start] = 0
    while heap:
        cost, current = h.heappop(heap)
        
        if d[current] < cost:
            continue
        
        for next_cost, next_node in g[current]:
            if d[next_node] > cost + next_cost:
                d[next_node] = cost + next_cost
                h.heappush(heap, (d[next_node], next_node))  # 갱신된 비용으로 힙에 추가

INF = 987654321
n = int(input())  # 노드의 개수
m = int(input())  # 간선의 개수

g = [[] for _ in range(n + 1)]  # 1-based 인덱스 사용
d = [INF] * (n + 1)

# 그래프 입력
for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().rstrip().split())
    g[s].append((c, e))
    

# 출발점과 도착점 입력
s, e = map(int, input().split())

# 다익스트라 실행
dijkstra(s)

# 결과 출력
print(d[e])
