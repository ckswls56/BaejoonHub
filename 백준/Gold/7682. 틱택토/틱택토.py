def is_end(board, player):
    # 가로, 세로 줄 확인
    for j in range(3):
        if board[0][j] == player and board[0][j] == board[1][j] == board[2][j]:
            return True
        if board[j][0] == player and board[j][0] == board[j][1] == board[j][2]:
            return True
    
    # 대각선 확인
    if board[1][1] == player:
        if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
            return True

    return False

strings = input()

while strings != 'end':
    x_count = strings.count('X')
    o_count = strings.count('O')
    
    # 판에 수를 채움
    b = [['.'] * 3 for _ in range(3)]
    idx = 0
    for i in range(3):
        for j in range(3):
            b[i][j] = strings[idx]
            idx += 1
    
    # X는 O보다 하나 더 많거나 같아야 함
    if not (x_count == o_count or x_count == o_count + 1):
        print("invalid")
    else:
        x_wins = is_end(b, 'X')
        o_wins = is_end(b, 'O')
        
        # 조건 검증
        if (x_wins and o_wins) or (x_wins and x_count == o_count) or (o_wins and x_count > o_count):
            print("invalid")
        elif x_wins or o_wins or x_count + o_count == 9:
            print("valid")
        else:
            print("invalid")
    
    strings = input()