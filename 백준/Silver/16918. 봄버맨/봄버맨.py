
def install_bomb(i,j,t):
    a[i][j] = t+3

r,c,n = map(int,input().split())

board = [list(input()) for _ in range(r)]

a = [[-1]*c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if board[i][j] == 'O':
            a[i][j] = 3


direction = [(-1,0),(1,0),(0,-1),(0,1)]

t = 1
flag = True
while t < n :
    t+=1 
    
    if flag:
        for i in range(r):
            for j in range(c):
                if a[i][j] == -1:
                    install_bomb(i,j,t)
        flag = not flag
    else :
        for i in range(r):
            for j in range(c):
                if a[i][j] == t:
                    a[i][j] = -1
                    for dy,dx in direction:
                        ny,nx = i+dy,j+dx
                        if 0<=ny<r and 0<=nx<c and a[ny][nx] != t:
                            a[ny][nx] = -1
        flag = not flag

for i in range(r):
    for j in range(c):
        if a[i][j] == -1:
            a[i][j] = '.'                     
        else :
            a[i][j] = 'O'
            
for aa in a:
    print("".join(aa))
