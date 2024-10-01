direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 방향: 위, 오른쪽, 아래, 왼쪽

c, r = map(int, input().split())  # 열(c)와 행(r) 입력
k = int(input())  # k번째 좌석 입력

if k > c * r:
    print(0)  # 좌석이 범위를 넘으면 0 출력
else:
    board = [[0 for _ in range(c)] for _ in range(r)]  # r x c 크기의 2차원 배열 생성
    d = 0  # 방향 인덱스
    y, x = r - 1, 0  # 시작 위치 (맨 아래 왼쪽)
    val = 1  # 채워질 값

    board[y][x] = val  # 첫 번째 값 채우기

    while val < r * c:
        dy, dx = direction[d][0], direction[d][1]
        ny, nx = y + dy, x + dx

        # 범위 내에 있고 아직 방문하지 않은 곳이면 이동
        if 0 <= ny < r and 0 <= nx < c and board[ny][nx] == 0:
            val += 1
            board[ny][nx] = val
            y, x = ny, nx
        else:
            d = (d + 1) % 4  # 방향 전환 (시계 방향)

    # k번째 좌석의 위치 찾기
    for i in range(r):
        for j in range(c):
            if board[i][j] == k:
                print(j + 1, r - i)  # 출력: 좌석 번호는 1부터 시작, 좌표계 반전
                break