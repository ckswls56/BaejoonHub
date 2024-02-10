def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    erase = True
    
    while erase:
        erase = False
        s = set()
        # check!
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i + 1 < len(board) and j + 1 < len(board[i]):
                    if board[i][j] != None and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1]:
                        s.add((i, j))
                        s.add((i + 1, j))
                        s.add((i, j + 1))
                        s.add((i + 1, j + 1))
                        erase = True
                        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i, j) in s:
                    board[i][j] = None
        
        # transpose
        board = list(zip(*board))

    
        for i in range(len(board)):
            board[i] = list(filter(lambda x: x is not None, board[i]))
            for j in range(n - len(board[i])):
                board[i].insert(0, None)
    
        board = [list(row) for row in zip(*board)]
        answer += len(s)
       

    return answer
