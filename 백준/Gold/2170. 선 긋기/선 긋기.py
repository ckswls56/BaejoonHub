import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (x[0], x[1]))
s,e = arr[0]
answer = 0
for a,b in arr[1:]:
    if e < a:
        answer += e - s
        s,e = a,b
    elif e < b:
        e = b
answer += e - s
    
print(answer)

    