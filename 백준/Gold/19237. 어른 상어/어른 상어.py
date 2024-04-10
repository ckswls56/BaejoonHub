n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]

priority = [[]for _ in range(m+1)]

shark_direction = list(map(int,input().split()))


for i in range(1,m+1):
    for _ in range(4):
        priority[i].append(list(map(int,input().split())))

smell = [[[] for _ in range(n)] for _ in range(n)]

total_cnt = m
time = 0
while time <= 1000:
    # print(board)
    # print()
    shark_cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                smell[i][j].append((board[i][j],time+k))
                shark_cnt+=1
    
    if shark_cnt == 1:
        break
    time += 1
    new_board = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            
            if board[i][j] != 0:
                flag = False
                d = shark_direction[board[i][j]-1] - 1
                for p in priority[board[i][j]][d]:
                    dy,dx = direction[p-1][0],direction[p-1][1]
                    ny,nx = dy+i,dx+j
                    if 0<=ny<n and 0<=nx<n :
                        if smell[ny][nx] == []:                            
                            if new_board[ny][nx] == 0 or new_board[ny][nx] > board[i][j]:
                                new_board[ny][nx] = board[i][j]
                                shark_direction[board[i][j]-1] = p
                            flag = True
                            break
                if not flag :                
                    for p in priority[board[i][j]][d]:
                        dy,dx = direction[p-1][0],direction[p-1][1]
                        ny,nx = dy+i,dx+j
                        if 0<=ny<n and 0<=nx<n :
                            for s,t in smell[ny][nx]:
                                if board[i][j] == s:
                                    if new_board[ny][nx] == 0 or new_board[ny][nx] > board[i][j] :
                                        new_board[ny][nx] = board[i][j]
                                        shark_direction[board[i][j]-1] = p
                                    break
                            else :
                                continue
                            break
    
    board = new_board
    for i in range(n):
        for j in range(n):
            if smell[i][j]:
                t = smell[i][j][0][1]
                if t <= time:
                    smell[i][j].pop(0)
    

if time <= 1000:
    print(time)
else :
    print(-1)          