import sys
from bisect import bisect_left
n, m = map(int, input().split())

d = dict()

# 칭호와 전투력 상한값 입력
for _ in range(n):
    s, number = sys.stdin.readline().rstrip().split()
    number = int(number)
    if number not in d:
        d[number] = s
        
award = list(d.keys())
award.sort()

# 캐릭터 전투력 입력 및 즉시 처리
for _ in range(m):
    power = int(sys.stdin.readline().rstrip())
    idx = bisect_left(award,power)
    print(d[award[idx]])