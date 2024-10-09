import sys
input = sys.stdin.readline
n, L = map(int, input().split())
pools = [list(map(int, input().split())) for _ in range(n)]
# 웅덩이 좌표 오름차순 정렬
pools.sort()

# 널빤지의 개수, 웅덩이를 덮은 널빤지의 마지막 위치 
res, s = 0, 0
for start, end in pools:
  s = max(start, s)
  diff = end - s
  count = (diff + L - 1) // L
  res += count
  s += count * L

print(res)