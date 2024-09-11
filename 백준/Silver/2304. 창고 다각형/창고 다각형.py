n = int(input())

lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append([a, b])

# 기둥을 x축 순으로 정렬
lst.sort()

# 가장 높은 기둥의 인덱스와 높이 구하기
max_height = max(lst, key=lambda x: x[1])
idx = lst.index(max_height)

# 왼쪽에서 가장 높은 기둥까지의 면적 계산
result = 0
height = lst[0][1]
for i in range(idx):
    if lst[i+1][1] > height:
        result += height * (lst[i+1][0] - lst[i][0])
        height = lst[i+1][1]
    else:
        result += height * (lst[i+1][0] - lst[i][0])

# 오른쪽에서 가장 높은 기둥까지의 면적 계산
height = lst[-1][1]
for i in range(n-1, idx, -1):
    if lst[i-1][1] > height:
        result += height * (lst[i][0] - lst[i-1][0])
        height = lst[i-1][1]
    else:
        result += height * (lst[i][0] - lst[i-1][0])

# 가장 높은 기둥의 면적을 더해준다
result += max_height[1]

print(result)