import sys

n, m = map(int, input().split())
map = {}

for i in range(n):
    text = sys.stdin.readline().rstrip()
    if len(text) < m:
        continue
    map.setdefault(text, 0)
    map[text] += 1
sorted_dict = dict(
    sorted(map.items(), key=lambda x: (-x[1], - len(x[0]), x[0])))

for i in sorted_dict:
    print(i)
