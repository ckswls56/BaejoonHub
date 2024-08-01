def check(arr):
    ret = 0
    cnt = 0
    for a in arr:
        if a == '.':
            cnt += 1
        else :
            cnt = 0
        
        if cnt == 2:
            ret += 1
            
    return ret
        
    

n = int(input())

inputs = [input().split() for _ in range(n)]
board = [row for rows in inputs for row in rows]

row = 0
col = 0

for i in range(n):
    row += check(board[i])
    
for cols in zip(*board):
    col += check(cols)
        
print(row, col)