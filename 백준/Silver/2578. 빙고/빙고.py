def check_cross():
    ret = 0
    
    if bingo[0][4] and bingo[1][3] and bingo[2][2] and bingo[3][1] and bingo[4][0]:
        ret += 1
    
    if bingo[0][0] and bingo[1][1] and bingo[2][2] and bingo[3][3] and bingo[4][4]:
        ret += 1

    return ret

def check_row():
    ret = 0
    for i in range(5):
        if all(bingo[i]):
            ret += 1
    
    return ret

def check_col():
    ret = 0
    for b in zip(*bingo):
        if all(b):
            ret += 1

    return ret


board = [list(map(int,input().split())) for _ in range(5)]
input_board = [list(map(int,input().split())) for _ in range(5)]

bingo = [list(0 for _ in range(5)) for _ in range(5)]

cord = dict()

for i in range(5):
    for j in range(5):
        cord[board[i][j]] = (i,j)

ans =0

for i in range(5):
    for j in range(5):
        ans += 1
        y,x = cord[input_board[i][j]]
        bingo[y][x] = 1
        rows,cols,cross =check_row(),check_col(),check_cross()
        
        if rows+cols+cross >= 3:
            print(ans)
            exit(0)