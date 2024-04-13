from collections import deque


# 가까운 승객 찾기
def find_near_customer(y,x):

    visited = [[False for _ in range(n)]for _ in range(n)]
    q = deque()
    q.append((y,x,0))
    possible = []
    while q :
        y,x,cost = q.popleft()
        
        if board[y][x] == 2:
            possible.append((y,x,cost))

        if visited[y][x] :
            continue
            
        visited[y][x] = True

        for dy,dx in direction:
            ny,nx = y+dy,x+dx
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and not board[ny][nx] == 1:
                q.append((ny,nx,cost+1))

    possible.sort(key = lambda x : (x[2],x[0],x[1]))
    if possible:
        return possible[0]
    else:
        return (-1,-1,-1)

def move_goal(y,x):
    visited = [[False for _ in range(n)]for _ in range(n)]
    q = deque()
    q.append((y,x,0))
    t_y,t_x = goal[(y,x)]
    while q :
        y,x,cost = q.popleft()
        
        if y == t_y and x == t_x:
            return (y,x,cost)

        if visited[y][x] :
            continue
            
        visited[y][x] = True

        for dy,dx in direction:
            ny,nx = y+dy,x+dx
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] and not board[ny][nx] == 1:
                q.append((ny,nx,cost+1))
    
    return (-1,-1,-1)




n,m,gas = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
goal = {}
taxi_y,taxi_x = map(lambda x : x-1,map(int,input().split()))

# 손님
for _ in range(m):
    c_y,c_x,t_y,t_x = map(lambda x : x-1,map(int,input().split()))
    board[c_y][c_x] = 2
    goal[(c_y,c_x)] = (t_y,t_x)

for _ in range(m):

    c_y,c_x,cost = find_near_customer(taxi_y,taxi_x)
    if c_y == -1:
        print(-1)
        exit(0)
    #탑승처리
    board[c_y][c_x] = 0
    taxi_y,taxi_x = c_y,c_x
    gas -= cost


    c_y,c_x,cost = move_goal(taxi_y,taxi_x)
    if c_y == -1:
        print(-1)
        exit(0)
    taxi_y,taxi_x = c_y,c_x
    gas -= cost

    if gas < 0 :
        print(-1)
        exit(0)
    gas += cost*2

print(gas)