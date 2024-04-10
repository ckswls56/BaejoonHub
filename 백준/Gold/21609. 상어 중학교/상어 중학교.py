from collections import deque

def bfs(y,x):

    blocks = []
    q = deque()
    rainbow = 0
    block = arr[y][x]
    q.append((y,x))
    
    while q:
        y,x = q.popleft()

        if visited[y][x]:
            continue
        
        if arr[y][x] == 0:
            rainbow += 1
        visited[y][x] = True
        blocks.append((y,x))

        for dy,dx in direction:
            ny,nx = y+dy,x+dx
            if 0<=ny<n and 0<=nx<n:
                if not visited[ny][nx] and arr[ny][nx] != -1 and (arr[ny][nx]==block or arr[ny][nx] == 0):
                    q.append((ny,nx))
    
    min_y,min_x = 100,100
    for y,x in blocks:
        if arr[y][x] == 0:
            visited[y][x] = False
        else:
            min_y=min(min_y,y)
            min_x=min(min_x,x)

    return (blocks,rainbow,min_y,min_x)

def gravity():

    for i in range(n-1,-1,-1):
        for j in range(n):
            if arr[i][j] == None:
                temp = 1
                while i-temp >= 0:
                    if arr[i-temp][j] == None:
                        temp+=1
                    elif arr[i-temp][j] >= 0 :
                        arr[i-temp][j],arr[i][j] = arr[i][j],arr[i-temp][j]
                        break
                    else :
                        break
                    
                    

n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]
ans = 0
while True :
    visited = [[False for _ in range(n)]for _ in range(n)]
    maxs_blocks = []
    rainbow_maxs = -1
    max_y,max_x = 0,0
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if arr[i][j] != -1 and arr[i][j] != None and arr[i][j]!= 0 and not visited[i][j]:
                blocks,rainbow,y,x = bfs(i,j)

                if len(blocks)-rainbow >= 1:
                    if len(blocks)>len(maxs_blocks):
                        maxs_blocks = blocks
                        rainbow_maxs = rainbow
                        max_y,max_x = y,x
                    elif len(blocks)==len(maxs_blocks) and rainbow>rainbow_maxs:
                        maxs_blocks = blocks
                        rainbow_maxs = rainbow
                        max_y,max_x = y,x
                    elif len(blocks)==len(maxs_blocks) and rainbow==rainbow_maxs:
                        if y>max_y:
                            maxs_blocks = blocks
                            rainbow_maxs = rainbow
                            max_y,max_x = y,x
                        elif y == max_y:
                            if x>max_x:
                                maxs_blocks = blocks
                                rainbow_maxs = rainbow
                                max_y,max_x = y,x


                        
    
    if len(maxs_blocks)<2:
        break

    ans += len(maxs_blocks)**2
    for y,x in maxs_blocks:
        arr[y][x] = None
    
    gravity()
    arr = list(map(list,zip(*arr)))[::-1]
    gravity()
    
    
print(ans)