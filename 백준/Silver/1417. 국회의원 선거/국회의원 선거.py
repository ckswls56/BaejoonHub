def check():
    # 첫 번째 값이 배열의 최대값이고, 그 최대값이 배열에서 유일한 경우에만 True를 반환
    return arr[0] == max(arr) and arr.count(max(arr)) == 1

n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

ans = 0

while not check():
    maxs = max(arr)

    for i in range(1, n):
        if arr[i] == maxs:
            arr[i] -= 1  # 최대값에서 하나 빼고
            arr[0] += 1  # 첫 번째 값에 하나 더함
            break

    ans += 1

print(ans)
