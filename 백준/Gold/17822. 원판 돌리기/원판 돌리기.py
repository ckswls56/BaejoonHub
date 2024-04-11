from collections import deque

def right(a, x):
    a.rotate(x)

def left(a, x):
    a.rotate(-x)

def bfs(circle,i,j):

    res = []
    q = deque()
    
    q.append((circle,i))

    while q :
        c,x = q.popleft()

        if visited[c][x]:
            continue
        
        visited[c][x] = True
        res.append((c,x))

        for dc,dx in direction:
            nc,nx = dc+c,(x+dx)%m
            if 0<=nc<n:
                if not visited[nc][nx] and board[nc][nx] == j:
                    q.append((nc,nx))
        
    
    if len(res)> 1 :
        for c,x in res:
            board[c][x] = 0
        return True
    
    return False
    

direction = [(-1,0),(1,0),(0,1),(0,-1)]
n,m,t = map(int,input().split())
board = [deque(map(int,input().split())) for _ in range(n)]

for _ in range(t):
    x,d,k = map(int,input().split())
    div = []
    for i in range(2,n+1):
        if i%x == 0:
            if d == 0:
                right(board[i-1],k)
            else :
                left(board[i-1],k)
            div.append(i-1)

    flag = False
    zeros = 0
    numbers = 0
    visited = [[False for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                if bfs(i,j,board[i][j]):
                    flag = True
                numbers+=board[i][j]
            else :
                zeros += 1
    
    if not flag :
        number_cnt = n*m-zeros
        if number_cnt == 0 :
            break
        avg = numbers / number_cnt
        
        for i in range(n):
            for j in range(m):
                if board[i][j] > 0:
                    if board[i][j] > avg :
                        board[i][j] -= 1
                    elif board[i][j] < avg :
                        board[i][j] += 1

ans = 0
for i in range(n):
    ans += sum(board[i])

print(ans)