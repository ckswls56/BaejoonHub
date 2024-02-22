import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())
    arr = []
    answer = []

    while len(arr) < m :
        s = list(map(int,input().split()))
        arr = arr + s
    
    for i in range(1,m+1,2):
        sub = arr[:i]
        sub.sort()
        answer.append(sub[i//2])

    print(len(answer))
    for i,a in enumerate(answer):
        print(a,end =" ")
        if (i+1) % 10 == 0:
            print()
    print()
