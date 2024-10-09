import sys


n = int(input())

arr = []

for _ in range(n):
    s,e = map(int,sys.stdin.readline().rstrip().split())
    arr.append((s,e))


ans = 0

b_s,b_e = arr[0]

for s,e in arr[1:]:
    if s <= b_e :
        # 겹치는 구간 처리 (최대값을 취함)
        b_e = max(b_e, e)
    else :
        ans += abs(b_e-b_s)
        b_s,b_e = s,e
    
ans += abs(b_e-b_s)

print(ans)
    