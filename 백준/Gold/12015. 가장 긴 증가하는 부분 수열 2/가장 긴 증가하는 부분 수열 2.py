import sys
input = sys.stdin.readline

s = []

n = int(input())
arr = list(map(int,input().split()))

for x in arr:
    if not s or s[-1]<x:
        s.append(x)
    elif s[-1]>x:
        # 이진탐색으로 x보다 큰 값 중 가장 작은 값 찾기
        left = 0
        right = len(s)-1
        while left<right:
            mid = (left+right)//2
            if s[mid]<x:
                left = mid+1
            else:
                right = mid
        s[right] = x



print(len(s))