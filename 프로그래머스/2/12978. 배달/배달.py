import heapq

def solution(N, road, K):
    g = [[] for _ in range(N+1)]
    
    for r in road:
        s, e, c = r[0], r[1], r[2]
        g[s].append((e, c))
        g[e].append((s, c))
        
    distance = [987654321] * (N+1)
    heap = []
    heapq.heappush(heap, (0, 1))  # 시작 노드: 1번
    
    while heap:
        dis, target = heapq.heappop(heap)
        
        if distance[target] < dis:
            continue
            
        distance[target] = dis
        for end,next_dis in g[target]:
            if dis + next_dis < distance[end]:
                heapq.heappush(heap, (dis + next_dis, end))
    
    count = 0
    for d in distance:
        if d <= K:
            count += 1
    
    return count