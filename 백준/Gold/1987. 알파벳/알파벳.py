direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def sol(arr, y, x):
    ret = 0
    
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        
        if 0 <= ny < r and 0 <= nx < c and board[ny][nx] not in arr:
            arr.add(board[ny][nx])
            ret = max(ret, sol(arr, ny, nx))
            arr.remove(board[ny][nx])
    
    return ret + 1  # 현재 칸을 포함하여 이동한 칸 수를 계산

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

# 초기 위치를 세트에 추가한 후 탐색 시작
start_set = set([board[0][0]])
print(sol(start_set, 0, 0))