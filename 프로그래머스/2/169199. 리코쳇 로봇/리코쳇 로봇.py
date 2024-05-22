from collections import deque

def solution(board):
    # Possible directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    q = deque()
    
    # Find the starting position 'R'
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                start = (i, j)
    
    # Initialize queue with the starting position and time = 0
    q.append((start[0], start[1], 0))
    # Visited matrix to track visited positions
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    
    while q:
        y, x, t = q.popleft()
        
        # If we reach the goal 'G', return the time taken
        if board[y][x] == 'G':
            return t
        if visited[y][x]:
            continue
        
        visited[y][x] = True
        
        # Explore all 4 directions
        for dy, dx in directions:
            ny, nx = y, x
            # Move in the current direction until hitting a wall or obstacle 'D'
            while 0 <= ny + dy < len(board) and 0 <= nx + dx < len(board[0]) and board[ny + dy][nx + dx] != 'D':
                ny += dy
                nx += dx
            
            
            q.append((ny, nx, t + 1))
    
    # If the goal 'G' is not reachable, return -1
    return -1
