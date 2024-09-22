from collections import deque

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    ## 패딩 중요!!
    board = [['.'] + list(input().rstrip()) + ['.'] for _ in range(h)]
    board = [['.'] * (w + 2)] + board + [['.'] * (w + 2)]
    keys = list(input().rstrip())

    cnt = 0

    q = deque()
    q.append((0, 0))
    visited = [[False] * (w + 2) for _ in range(h + 2)]

    while q:
        y, x = q.popleft()
        visited[y][x] = True

        for dy, dx in direction:
            ny, nx = y + dy, x + dx

            # 범위 검사 및 벽, 방문 여부 확인
            if not (0 <= ny < h + 2 and 0 <= nx < w + 2) or board[ny][nx] == '*' or visited[ny][nx]:
                continue

            # 문을 만났을 경우
            if 'A' <= board[ny][nx] <= 'Z':
                if board[ny][nx].lower() not in keys:
                    continue
                else:
                    board[ny][nx] = '.'  # 문을 연 후 빈 공간으로 변경

            # 열쇠를 만났을 경우
            elif 'a' <= board[ny][nx] <= 'z':
                keys.append(board[ny][nx])
                board[ny][nx] = '.'
                visited = [[False] * (w + 2) for _ in range(h + 2)]  # 방문 배열 초기화

            # 문서를 만났을 경우
            elif board[ny][nx] == '$':
                cnt += 1
                board[ny][nx] = '.'  # 문서를 수집한 후 빈 공간으로 변경

            # 탐색할 위치 추가
            q.append((ny, nx))
            visited[ny][nx] = True

    print(cnt)
