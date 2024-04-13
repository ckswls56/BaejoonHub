from collections import deque

def rotate(a,c):
    l = 2**c
    for i in range(0,2**n,l):
        for j in range(0,2**n,l):
            temp = []
            for k in range(l):
                temp.append(a[i+k][j:j+l])
            temp = list(zip(*temp[::-1]))
            for k in range(l):
                a[i+k][j:j+l]=temp[k]
        
def reduce(a):
    temp = [[0]*2**n for _ in range(2**n)]
    for i in range(2**n):
        for j in range(2**n):
            cnt = 0
            for dy,dx in direction:
                ny,nx = i+dy,j+dx
                if 0<=ny<2**n and 0<=nx<2**n:
                    if a[ny][nx]>0:
                        cnt+=1
            if cnt<=2 and a[i][j]>0:
                temp[i][j]-=1
    
    for i in range(2**n):
        for j in range(2**n):
            a[i][j]+= temp[i][j]

def bfs(y,x):
    q=deque()
    q.append((y,x))
    visited.add((y,x))
    cnt = 1
    while q:
        y,x = q.popleft()
        for dy,dx in direction:
            ny,nx = y+dy,x+dx

            if 0<=ny<2**n and 0<=nx<2**n:
                if (ny,nx) not in visited and a[ny][nx]!=0:
                    q.append((ny,nx))
                    visited.add((ny,nx))
                    cnt+=1
    
    return cnt


visited = set()
n,q = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(2**n)]
q_arr = list(map(int,input().split()))
direction = [(1,0),(-1,0),(0,-1),(0,1)]

for c in q_arr:
    rotate(a,c)
    reduce(a)

answer = 0
max_ans = 0

for i in range(2**n):
    for j in range(2**n):
        if a[i][j]>0:
            answer+=a[i][j]
            max_ans=max(max_ans,bfs(i,j))

print(answer)
print(max_ans)