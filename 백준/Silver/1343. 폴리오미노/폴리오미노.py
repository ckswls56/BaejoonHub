def check():
    for b in board:
        if b == 'X':
            return False
    
    return True

def dfs(i):
    
    if i>= len(board):
        if check():
            return True
        
    if board[i] == '.':
        if dfs(i+1):
            return True
        else :
            return False
    
    
    if i+3<len(board):
        if board[i] == 'X' and board[i] == board[i+1] == board[i+2] == board[i+3]:
            board[i] = board[i+1] = board[i+2] = board[i+3] = 'A'
            if dfs(i+4):
                return True
            board[i] = board[i+1] = board[i+2] = board[i+3] = 'X'
    if i+1<len(board):
        if board[i] == 'X' and board[i] == board[i+1]:
            board[i] = board[i+1] = 'B'
            if dfs(i+2):
                return True
            board[i] = board[i+1] = 'X'
        
            
    

board = [ a for a in input()]
if dfs(0):
    print("".join(map(str,board)))
else :
    print(-1)