from itertools import combinations
import copy
def check_board():
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                return False
    
    return True

def get_distance(r1,r2,c1,c2):
    return abs(r1-r2)+abs(c1-c2)

def move():
    zeros = [0 for _ in range(m)]
    
    for i in range(n-1,0,-1):
        board[i] = board[i-1]
    
    board[0] = zeros
    
def get_possible_enemey(y,x):
    possible = []
    
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                pos = get_distance(y,i,x,j)
                if pos <= d:
                    possible.append((pos,i,j))

    possible.sort(key = lambda x:(x[0],x[2]))
    
    if possible:
        return (possible[0][1],possible[0][2])
    else:
        return (-1,-1)
                
            


n,m,d = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
board.append([0 for _ in range(m)])
copy_board = copy.deepcopy(board)

possible_archors = list(combinations([i for i in range(m)],3))
ans = 0

for archors in possible_archors:
    
    killed_enemy = 0
    # set archors
    for i in archors:
        board[-1][i] = 1
    
    while not check_board():
        
        remove_enemey = set()
        for archor in archors:
            pos = get_possible_enemey(n,archor)
            if pos != (-1,-1):
                remove_enemey.add(pos)
        
        killed_enemy+= len(remove_enemey)
        
        for y,x in remove_enemey:
            board[y][x] = 0
        move()
        
        
    board = copy_board
    copy_board = copy.deepcopy(board)
    
    ans = max(killed_enemy,ans)

print(ans)