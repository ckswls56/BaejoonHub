from bisect import bisect_left

def check(k):
    l = bisect_left(arr, k)
    s = sum(arr[:l]) + (n - l) * k
    return s <= m

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())

if sum(arr) <= m:
    print(max(arr))
    exit(0)

l, r = 0, max(arr)

while l <= r:
    mid = (l + r) // 2
    if check(mid):
        l = mid + 1
    else:
        r = mid - 1

print(r)
