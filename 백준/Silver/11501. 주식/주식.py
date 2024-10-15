import sys
from bisect import bisect_left
T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(reversed(list(map(int,sys.stdin.readline().rstrip().split()))))
    maxs = arr[0]
    ans = 0
    for i in range(1,len(arr)):
        if maxs < arr[i]:
            maxs = arr[i]
        elif maxs > arr[i]:
            ans += maxs - arr[i]
            

    print(ans)