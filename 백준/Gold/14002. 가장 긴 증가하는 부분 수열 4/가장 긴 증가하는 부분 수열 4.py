import sys
input = sys.stdin.readline

def print_path():
    
    max_length = max(dp)
    max_index = dp.index(max_length)
    result = [arr[max_index]]
    for i in range(max_index - 1, -1, -1):
        if arr[i] < arr[max_index] and dp[i] == dp[max_index] - 1:
            result.append(arr[i])
            max_index = i

    result.reverse()
    print(len(result))
    print(*result)


n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print_path()
