from itertools import permutations

def check(arr,a,b):
    cnt = 0
    for i in arr:
        if a==i:
            break
        elif i>a:
            cnt += 1

    if cnt != b:
        return False
    else:
        return True

n = int(input())
arr = [i for i in range(1,n+1)]
l = list(map(int,input().split()))

for p in permutations(arr):
    for a in p:
        if not check(p,a,l[a-1]):
            break
    else :
        print(*p)