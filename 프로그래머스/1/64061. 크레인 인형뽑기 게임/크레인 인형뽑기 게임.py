def findNotZero(l):
    for i,item in enumerate(l) :
        if item != 0:
            return i
    return len(l)-1

from collections import deque
def solution(board, moves):
    answer = 0
    stack = deque()
    new_board = [list(row) for row in zip(*board)]
    
    
    for m in moves :
        notZeroIndex = findNotZero(new_board[m-1])
        if new_board[m-1][notZeroIndex] != 0:
            if stack and stack[-1] == new_board[m-1][notZeroIndex]:
                stack.pop()
                answer += 2
            else:
                stack.append(new_board[m-1][notZeroIndex])
            new_board[m-1][notZeroIndex] = 0
        
    return answer