# 이동 방향 정의 (오른쪽, 왼쪽, 아래, 위, 제자리에 머무름)
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
INFINITY = float('inf')  # 가독성을 높이기 위해 float('inf') 사용
WALL = 5  # 미로에서 벽을 나타냄

def solution(maze):
    # 목표 마커
    R_GOAL, B_GOAL = 3, 4
    
    # 초기 위치 초기화
    r_cur = b_cur = R_GOLE_POS = B_GOLE_POS = (0, 0)
    
    # 미로의 크기
    rows, cols = len(maze), len(maze[0])

    # 초기 및 목표 위치 찾기
    for x in range(rows):
        for y in range(cols):
            if maze[x][y] == 1:  # 빨간 공 시작 위치
                r_cur = (x, y)
            elif maze[x][y] == 2:  # 파란 공 시작 위치
                b_cur = (x, y)
            elif maze[x][y] == R_GOAL:  # 빨간 공 목표 위치
                r_goal = (x, y)
            elif maze[x][y] == B_GOAL:  # 파란 공 목표 위치
                b_goal = (x, y)

    # 빨간 공과 파란 공의 방문 위치
    r_vis = [[False] * cols for _ in range(rows)]
    b_vis = [[False] * cols for _ in range(rows)]
    
    # 초기 위치를 방문한 것으로 표시
    r_vis[r_cur[0]][r_cur[1]], b_vis[b_cur[0]][b_cur[1]] = True, True

    def out_of_bounds(x, y):
        """좌표가 미로의 경계를 벗어나는지 확인."""
        return x < 0 or y < 0 or x >= rows or y >= cols

    def is_visited(vis, goal, x, y):
        """위치가 방문되었는지 및 목표가 아닌지 확인."""
        return maze[x][y] != goal and vis[x][y]

    def is_duplicate(x1, y1, x2, y2):
        """두 위치가 같은지 확인."""
        return x1 == x2 and y1 == y2

    def is_crossed(cur1, cur2, next1, next2):
        """두 공의 현재 위치와 다음 위치가 교차하는지 확인."""
        return cur1 == next2 and cur2 == next1

    def dfs(r_cur, b_cur, r_vis, b_vis, count):
        """모든 경로를 탐색하기 위한 깊이 우선 탐색."""
        nonlocal ans  # 범위 외부에서 정의된 ans를 수정하기 위해 사용
        if r_cur == r_goal and b_cur == b_goal:
            ans = min(ans, count)
            return

        for d_rx, d_ry in DIRECTIONS:
            # 빨간 공 이동
            rx_next, ry_next = r_cur[0] + d_rx, r_cur[1] + d_ry
            
            # 빨간 공의 다음 이동이 유효하지 않으면 건너뜀
            if out_of_bounds(rx_next, ry_next) or is_visited(r_vis, R_GOAL, rx_next, ry_next) or maze[rx_next][ry_next] == WALL:
                continue
            
            # 빨간 공의 새로운 위치를 방문한 것으로 표시
            r_vis[rx_next][ry_next] = True

            for d_bx, d_by in DIRECTIONS:
                # 파란 공의 제자리에 머무르는 이동은 건너뜀
                # if (d_rx, d_ry) == (0, 0) and (d_bx, d_by) == (0, 0):
                #     break
                
                # 파란 공 이동
                bx_next, by_next = b_cur[0] + d_bx, b_cur[1] + d_by
                
                # 파란 공의 다음 이동이 유효하지 않으면 건너뜀
                if (out_of_bounds(bx_next, by_next) or 
                    is_visited(b_vis, B_GOAL, bx_next, by_next) or 
                    maze[bx_next][by_next] == WALL or 
                    is_duplicate(bx_next, by_next, rx_next, ry_next) or 
                    is_crossed(r_cur, b_cur, (rx_next, ry_next), (bx_next, by_next))):
                    continue
                
                # 파란 공의 새로운 위치를 방문한 것으로 표시
                b_vis[bx_next][by_next] = True
                
                # 업데이트된 위치와 카운트로 DFS 계속 진행
                dfs((rx_next, ry_next), (bx_next, by_next), r_vis, b_vis, count + 1)
                
                # 되돌리기: 파란 공의 위치를 미방문으로 설정
                b_vis[bx_next][by_next] = False
            
            # 되돌리기: 빨간 공의 위치를 미방문으로 설정
            r_vis[rx_next][ry_next] = False

    ans = INFINITY
    dfs(r_cur, b_cur, r_vis, b_vis, 0)
    return 0 if ans == INFINITY else ans
