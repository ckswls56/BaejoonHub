from collections import deque

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

q = deque()
t = 0
i = 0
current_weight = 0

while i < n or q:
    t += 1
    
    # 다리를 다 건넌 트럭 제거
    if q and t - q[0][1] == w:
        current_weight -= q.popleft()[0]
    
    # 새로운 트럭 추가 가능 여부 확인
    if i < n and current_weight + trucks[i] <= l and len(q) < w:
        q.append((trucks[i], t))
        current_weight += trucks[i]
        i += 1

print(t)
