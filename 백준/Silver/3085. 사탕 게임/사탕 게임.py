direction = [(-1,0),(1,0),(0,-1),(0,1)]

def row_check(string):
    before = string[0]
    ret = 1
    temp = 1
    for i in range(1, len(string)):
        if before == string[i]:
            temp += 1
        else:
            ret = max(ret, temp)
            temp = 1
            before = string[i]
    return max(ret, temp)

def check():
    ret = 0
    for i in range(n):
        ret = max(ret, row_check(board[i]))
    
    for string in zip(*board):
        ret = max(ret, row_check(string))
    
    return ret

n = int(input())
input_strings = [input() for _ in range(n)]

board = []

for arr in input_strings:
    temp = []
    for a in arr:
        temp.append(a)
    board.append(temp)

res = check()

for y in range(n):
    for x in range(n):
        for dy, dx in direction:
            cy, cx = dy + y, dx + x
            if 0 <= cy < n and 0 <= cx < n:
                # Swap elements
                board[y][x], board[cy][cx] = board[cy][cx], board[y][x]
                res = max(res, check())
                # Swap back to original position
                board[y][x], board[cy][cx] = board[cy][cx], board[y][x]
        if res == n :
            break

print(res)