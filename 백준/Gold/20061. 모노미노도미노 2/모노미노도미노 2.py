

def gravity_v(t,y,x):
    idx = 1
    if t==1:
        while y+idx <9 and not board[y+idx][x]:
            idx += 1
        if board[y+idx][x]:
            idx -= 1
        board[y+idx][x] = True
    elif t==2:
        while y+idx <9 and not board[y+idx][x] and not board[y+idx][x+1]:
            idx += 1
        if board[y+idx][x] or board[y+idx][x+1]:
            idx -= 1
        board[y+idx][x] = True
        board[y+idx][x+1] = True
    else :
        while y+idx+1 <9 and not board[y+idx][x] and not board[y+idx+1][x]:
            idx += 1
        if board[y+idx][x] or board[y+idx+1][x]:
            idx -= 1
        board[y+idx][x] = True
        board[y+idx+1][x] = True

def gravity_h(t,y,x):
    idx = 1
    if t==1:
        while x+idx <9 and not board[y][x+idx]:
            idx += 1
        if board[y][x+idx]:
            idx -= 1
        board[y][x+idx] = True
    elif t==2:
        while x+idx+1 <9 and not board[y][x+idx] and not board[y][x+idx+1]:
            idx += 1
        if board[y][x+idx] or board[y][x+idx+1]:
            idx -= 1
        board[y][x+idx] = True
        board[y][x+idx+1] = True
    else :
        while x+idx <9 and not board[y][x+idx] and not board[y+1][x+idx]:
            idx += 1
        if board[y][x+idx] or board[y+1][x+idx]:
            idx -= 1
        board[y][x+idx] = True
        board[y+1][x+idx] = True


n = int(input())

board = [[False for _ in range(10)]for _ in range(10)]
score = 0

for _ in range(n):
    t,x,y = map(int,input().split())
    gravity_v(t,x,y)
    gravity_h(t,x,y)
    flag  = True
    while flag :
        flag = False
        for i in range(9,5,-1):
            if all(board[i][:4]):
                flag = True
                score += 1
                for j in range(4):
                    board[i][j] = False
                idx = 0
                while i-idx-1>4:
                    board[i-idx],board[i-idx-1] = board[i-idx-1],board[i-idx]
                    idx += 1
                break
    
    flag = True
    while flag :
        flag = False
        for j in range(9,5,-1):
            for i in range(4):
                if not board[i][j]:
                    break
            else :
                flag = True
                for i in range(4):
                    board[i][j] = False
                score += 1
                idx = 0
                while j-idx-1>4:
                    for i in range(4):
                        board[i][j-idx],board[i][j-idx-1] =board[i][j-idx-1] , board[i][j-idx]
                    idx += 1
                
            
    
    cnt = 0
    for i in range(4,6):
        if any(board[i][:4]):
            cnt+=1
    
    if cnt>=1:
        for i in range(cnt):
            for j in range(4):
                board[9-i][j] = False
        idx = 9
        while idx-cnt>3:
                    board[idx],board[idx-cnt] = board[idx-cnt],board[idx]
                    idx -= 1
        
        for i in range(4,6):
            for j in range(4):
                board[i][j] = False

    
    cnt = 0
    for j in range(4,6):
        for i in range(4):
            if board[i][j]:
                cnt += 1
                break
    
    if cnt>=1:
        for j in range(cnt):
            for i in range(4):
                board[i][9-j] = False

        idx = 9
        while idx-cnt>3:
            for i in range(4):
                board[i][idx],board[i][idx-cnt] = board[i][idx-cnt],board[i][idx]
            idx -= 1
        
        for j in range(4,6):
            for i in range(4):
                board[i][j] = False


print(score)
blue = 0
green = 0
for i in range(4):
    for j in range(6,10):
        if board[i][j]:
            blue += 1

for j in range(4):
    for i in range(6,10):
        if board[i][j]:
            green += 1
print(blue+green)