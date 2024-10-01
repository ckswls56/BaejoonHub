def sol(arr, y, s, start):
    # 모든 도시를 방문한 경우 출발점으로 돌아가는 비용 추가
    if len(arr) == n:
        return s + cost[y][start] if cost[y][start] > 0 else float('inf')  # 출발점으로 돌아갈 수 없는 경우 처리
    
    ret = float('inf')
    
    # 다음 방문할 도시 탐색
    for i in range(n):
        if i not in arr and cost[y][i] > 0:  # 방문하지 않은 도시와 경로가 존재하는지 확인
            arr.add(i)
            ret = min(ret, sol(arr, i, s + cost[y][i], start))
            arr.remove(i)
    
    return ret

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')
# 각 도시를 출발점으로 설정해 탐색
for i in range(n):
    start = i
    ans = min(ans, sol(set([i]), i, 0, start))

print(ans if ans != float('inf') else -1)  # 경로가 없는 경우 처리
