from collections import deque
import itertools

virus = []
n,m = map(int,input().split())
direction = [[-1,0],[1,0],[0,1],[0,-1]]

visited = [[False] * m for _ in range(n)]

def initialize_visited():
    n = len(visited)
    m = len(visited[0])

    for i in range(n):
        for j in range(m):
            visited[i][j] = False
    




arr = []

for i in range(n):
        arr.append(list(map(int,input().split())))

for i in range(n):
        for j in range(m) :
                if arr[i][j] == 2 :
                        point = i,j
                        virus.append(point)

min = 0           

zeros = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 0:
            zeros.append((i, j))

combinations = list(itertools.combinations(zeros, 3))

for comb in combinations:
    copy_arr = [row[:] for row in arr]  # arr 배열을 복사하여 변경된 배열을 저장

    for i, j in comb:
        copy_arr[i][j] = 1

    initialize_visited()
    for p in virus :
        q= deque()
        q.append(p)

        while(q) :
            c = q.pop()
            x,y = c[1],c[0]
            visited[y][x] = True
            copy_arr[y][x] = 2

            for dx,dy in direction :
                if( x+dx >= 0 and x+dx < m and y+dy >= 0 and y+dy < n ):
                        if(visited[y+dy][x+dx] == False and copy_arr[y+dy][x+dx] == 0):
                                next = y+dy,x+dx
                                q.append(next)
    sum = 0
    #print(copy_arr)
    for i in copy_arr :
         sum += i.count(0)
    if sum > min :
          min = sum


print(min)