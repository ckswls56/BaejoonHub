def check_all():
    flag = False
    row_temp = set()
    col_temp = set()
    for i in range(9):
        for j in range(9):
            row_temp.add(board[i][j])
            col_temp.add(board[j][i])
        
        if len(row_temp) != 9 or len(col_temp) != 9:
            flag = True
            break
        
        row_temp.clear()
        col_temp.clear()
    
    sqare_temp = set()
    for k in range(0, 9, 3): # y축 변화량
        for l in range(0, 9, 3): # x축 변화량
            for i in range(3):
                for j in range(3):
                    sqare_temp.add(board[k + i][l + j])
            
            if len(sqare_temp) != 9:
                flag = True
                break
            sqare_temp.clear()
        if flag:
            break
    
    return not flag

def check_row(y, target):
    return target not in board[y]

def check_col(x, target):
    return all(board[i][x] != target for i in range(9))

def check_square(x, y, target):
    x0, y0 = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if board[y0 + i][x0 + j] == target:
                return False
    return True

def dfs(cnt):
    if cnt == len(zeros):
        return check_all()
    
    y, x = zeros[cnt]
    for i in range(1, 10):
        if check_row(y, i) and check_col(x, i) and check_square(x, y, i):
            board[y][x] = i
            if dfs(cnt + 1):
                return True
            board[y][x] = 0 # 다시 board 복구
    return False

inputs = [input() for _ in range(9)]
board = [list(map(int, row)) for row in inputs]

zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

if dfs(0):
    for row in board:
        print(''.join(map(str, row)))
