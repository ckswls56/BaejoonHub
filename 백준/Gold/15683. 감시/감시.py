from itertools import permutations

def get_change(maps,y,x,dir):
    dy,dx = dir[0],dir[1]
    ny,nx = y+dy,x+dx
    res = 0
    while 0<=ny<n and 0<=nx<m:
        if maps[ny][nx] == 6:
            break
        elif 1<= maps[ny][nx] <= 5:
            ny,nx = ny+dy,nx+dx
        else :
            if maps[ny][nx] != -1:
                res += 1
            ny,nx = ny+dy,nx+dx
            
            
    return res

def change_maps(maps,y,x,dir):
    dy,dx = dir[0],dir[1]
    ny,nx = y+dy,x+dx
    res = 0
    while 0<=ny<n and 0<=nx<m:
        if maps[ny][nx] == 6:
            break
        elif 1<= maps[ny][nx] <= 5:
            ny,nx = ny+dy,nx+dx
        else :
            maps[ny][nx] = -1
            ny,nx = ny+dy,nx+dx
            res += 1
    return res

def get_min_maps(maps,y,x):

    if maps[y][x] == 1:
        ret = -1
        idx = -1
        for i,dir in enumerate(direction):
            temp = get_change(maps,y,x,dir)
            if ret < temp:
                idx = i
                ret = temp
        change_maps(maps,y,x,direction[idx])
        
    elif maps[y][x] == 2:
        verti,hori = get_change(maps,y,x,direction[0])+get_change(maps,y,x,direction[1]),get_change(maps,y,x,direction[2])+get_change(maps,y,x,direction[3])
        if verti > hori :
            change_maps(maps,y,x,direction[0])
            change_maps(maps,y,x,direction[1])
        else :
            change_maps(maps,y,x,direction[2])
            change_maps(maps,y,x,direction[3])
    elif maps[y][x] == 3:
        #ㄴ 모양
        one = get_change(maps,y,x,direction[0])+get_change(maps,y,x,direction[2])
        two = get_change(maps,y,x,direction[1])+get_change(maps,y,x,direction[2])
        three = get_change(maps,y,x,direction[1])+get_change(maps,y,x,direction[3])
        four = get_change(maps,y,x,direction[0])+get_change(maps,y,x,direction[3])
        maxs = max(max(max(one,two),three),four)
        if one == maxs:
            change_maps(maps,y,x,direction[0])
            change_maps(maps,y,x,direction[2])
        elif two == maxs:
            change_maps(maps,y,x,direction[1])
            change_maps(maps,y,x,direction[2])
        elif three == maxs:
            change_maps(maps,y,x,direction[1])
            change_maps(maps,y,x,direction[3])
        else :
            change_maps(maps,y,x,direction[0])
            change_maps(maps,y,x,direction[3])
    elif maps[y][x] == 4:
        #ㅏ 모양
        one = get_change(maps,y,x,direction[0])+get_change(maps,y,x,direction[2])+get_change(maps,y,x,direction[3])
        two = get_change(maps,y,x,direction[0])+get_change(maps,y,x,direction[1])+get_change(maps,y,x,direction[2])
        three = get_change(maps,y,x,direction[1])+get_change(maps,y,x,direction[2])+get_change(maps,y,x,direction[3])
        four = get_change(maps,y,x,direction[0])+get_change(maps,y,x,direction[1])+get_change(maps,y,x,direction[3])
        maxs = max(max(max(one,two),three),four)
        if one == maxs:
            change_maps(maps,y,x,direction[0])
            change_maps(maps,y,x,direction[2])
            change_maps(maps,y,x,direction[3])
        elif two == maxs:
            change_maps(maps,y,x,direction[0])
            change_maps(maps,y,x,direction[1])
            change_maps(maps,y,x,direction[2])
        elif three == maxs:
            change_maps(maps,y,x,direction[1])
            change_maps(maps,y,x,direction[2])
            change_maps(maps,y,x,direction[3])
        else :
            change_maps(maps,y,x,direction[0])
            change_maps(maps,y,x,direction[1])
            change_maps(maps,y,x,direction[3])
    
    else :
        for dy,dx in direction:
            ny,nx = y+dy,x+dx
            while 0<=ny<n and 0<=nx<m:
                if maps[ny][nx] == 6:
                    break
                elif 1<= maps[ny][nx] <= 5:
                    ny,nx = ny+dy,nx+dx
                else :
                    maps[ny][nx] = -1
                    ny,nx = ny+dy,nx+dx
                    
                

def get_blind_spit(maps):
    ret = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                ret+=1

    return ret

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]
cctv = []
answer = 10000
for i in range(n):
    for j in range(m):
        if 1<=arr[i][j]<=5:
            cctv.append((i,j))

for permutation in permutations(cctv):
    temp = [row[:] for row in arr]
    for y,x in permutation:
        get_min_maps(temp,y,x)
    answer = min(answer,get_blind_spit(temp))
    if answer == 0:
        break
    
print(answer)