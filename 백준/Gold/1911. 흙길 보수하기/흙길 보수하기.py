import sys
input = sys.stdin.readline
n, L = map(int, input().split())
pools = [list(map(int, input().split())) for _ in range(n)]
# 웅덩이 좌표 오름차순 정렬
pools.sort()

# 웅덩이를 덮은 마지막 널빤지의 위치 
cur = 0
# 널빤지의 개수 
cnt = 0
for start, end in pools:
    
    # 이전 웅덩이에서 덮은 널빤지가 해당 웅덩이를 덮고있는 경우 
    if cur > start:
        start = cur
    # 널빤지의 개수 카운트 
    while start < end:
        start += L
        cnt += 1
    cur = start

print(cnt)