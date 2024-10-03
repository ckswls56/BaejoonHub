import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

# dp_table: 가장 긴 증가하는 부분 수열을 저장하는 배열
dp_table = [-float('inf')]
store = []

# LIS 배열을 만들면서 각 위치 저장
for num in L:
    if dp_table[-1] < num:
        dp_table.append(num)
        store.append((len(dp_table) - 1, num))  # (LIS 길이, 숫자) 저장
    else:
        pos = bisect_left(dp_table, num)
        dp_table[pos] = num
        store.append((pos, num))

# LIS 길이 출력
lis_length = len(dp_table) - 1
print(lis_length)

# LIS 추적하여 결과 출력
result = []
index = lis_length
for pos, num in reversed(store):
    if pos == index:
        result.append(num)
        index -= 1

print(*reversed(result))
