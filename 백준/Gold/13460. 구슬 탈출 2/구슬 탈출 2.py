from collections import deque

n,m = map(int, input().split())
arr = [list(map(str,input())) for _ in range(n)]

res = -1

q = deque()
dir = [[-1,0],[1,0],[0,-1],[0,1]]

blue_start = 0,0
red_start = 0,0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'B':
            blue_start = i,j
        if arr[i][j] == 'R':
            red_start = i,j

q.append((blue_start,red_start,0))
visited = set()

while q:
    blue, red, cnt = q.popleft()
    
    if cnt > 10:
        res = -1
        break
    if arr[blue[0]][blue[1]] == 'O':
        continue
    if arr[red[0]][red[1]] == 'O':
        res = cnt
        break
    for i in range(4):
        blue_next = blue
        red_next = red
        while True:
            blue_next = blue_next[0] + dir[i][0], blue_next[1] + dir[i][1]
            if arr[blue_next[0]][blue_next[1]] == 'O':
                break
            if arr[blue_next[0]][blue_next[1]] == '#':
                blue_next = blue_next[0] - dir[i][0], blue_next[1] - dir[i][1]
                break
        while True:
            red_next = red_next[0] + dir[i][0], red_next[1] + dir[i][1]
            if arr[red_next[0]][red_next[1]] == 'O':
                break
            if arr[red_next[0]][red_next[1]] == '#':
                red_next = red_next[0] - dir[i][0], red_next[1] - dir[i][1]
                break
        if blue_next == red_next:
            if arr[red_next[0]][red_next[1]] != 'O':
                blue_dist = abs(blue_next[0] - blue[0]) + abs(blue_next[1] - blue[1])
                red_dist = abs(red_next[0] - red[0]) + abs(red_next[1] - red[1])
                if blue_dist > red_dist:
                    blue_next = blue_next[0] - dir[i][0], blue_next[1] - dir[i][1]
                else:
                    red_next = red_next[0] - dir[i][0], red_next[1] - dir[i][1]
            else :
                continue
        ## blue나 red가 방문하지 않은 곳만 q에 추가
        if (blue_next, red_next) not in visited:
            visited.add((blue_next, red_next))
            q.append((blue_next, red_next, cnt+1))

print(res)