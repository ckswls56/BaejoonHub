import math
n = int(input())
arr = list(map(int,input().split()))
b,c = map(int,input().split())
answer = 0
for a in arr :
    a-=b
    answer += 1
    if a>0:
        answer += math.ceil(a/c)

print(answer)

