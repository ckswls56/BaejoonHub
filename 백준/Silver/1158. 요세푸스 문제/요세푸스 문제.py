from collections import deque

res = []

n, k = map(int, input().split())
queue = deque()

cnt = 0
total = 1

while len(res) != n:
    while cnt != k:
        if total <= n:
            queue.append(total)
        else:
            queue.append(queue.popleft())
        total += 1
        cnt += 1
    res.append(queue.pop())
    cnt = 0

print("<", end="")
for i in res:
    if i == res[-1]:
        print(i, end="")
    else:
        print(i, end=", ")

print(">", end="")
