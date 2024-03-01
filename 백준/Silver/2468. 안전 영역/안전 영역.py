def dfs(y, x, size):
    stack = [(y, x)]
    visited[y][x] = True
    connected_area_count = 0  # 연결된 영역의 개수

    while stack:
        y, x = stack.pop()
        connected_area_count += 1  # 방문한 좌표의 개수를 연결된 영역의 개수로 취급
        for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and arr[ny][nx] > size:
                stack.append((ny, nx))
                visited[ny][nx] = True
    
    return connected_area_count  # 연결된 영역의 개수 반환

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_height = max(max(sub) for sub in arr)
answer = 1

for k in range(1, max_height):
    temp = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > k:
                dfs(i, j, k)
                temp += 1
    answer = max(answer, temp)

print(answer)