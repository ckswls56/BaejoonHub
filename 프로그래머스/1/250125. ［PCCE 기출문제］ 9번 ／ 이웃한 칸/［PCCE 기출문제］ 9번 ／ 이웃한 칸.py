def solution(board, h, w):
    answer = 0
    d = [(1,0),(-1,0),(0,-1),(0,1)]
    
    for i in range(4):
        dy,dx = h+d[i][0],w+d[i][1]
        if 0<=dy<len(board) and 0<=dx<len(board):
            if board[dy][dx] == board[h][w]:
                answer+=1
        
    return answer