n, m = map(int, input().split())

# 입력을 문자 단위로 처리
inputs = [list(input()) for _ in range(n)] 

visited = [[False for _ in range(m)] for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            ans += 1
            visited[i][j] = True
            if inputs[i][j] == '-':
                # 가로로 연결된 부분 탐색
                nj = j + 1
                while nj < m and inputs[i][nj] == '-':
                    visited[i][nj] = True
                    nj += 1
            else:
                # 세로로 연결된 부분 탐색
                ni = i + 1
                while ni < n and inputs[ni][j] == '|':
                    visited[ni][j] = True
                    ni += 1

print(ans)
