import sys
input=sys.stdin.readline
from collections import deque

#공기 탐색
def air_bfs(i,j):
    q=deque()
    q.append([i,j])
    visited[i][j]=1

    while q:
        x,y=q.popleft()
        for dy,dx in direction:
            ny,nx = y+dy,x+dx
            if 0<=nx<n and 0<=ny<m:
            	#다음 진행이 공기면(큐 추가, 방문처리)
                if visited[nx][ny]==0 and board[nx][ny]==0:
                    q.append([nx,ny])
                    visited[nx][ny]=1
                #다음 진행이 치즈면(방문정보 업데이트)
                elif board[nx][ny]==1:
                    visited[nx][ny]=visited[nx][ny]+1

n, m=map(int, input().split())
board=[]
for i in range(n):
    board.append(list(map(int, input().split())))

direction = [(-1,0),(1,0),(0,1),(0,-1)]
time=0

while 1:
    visited=[[0 for _ in range(m)] for _ in range(n)]

    air_bfs(0,0)
    #탐색 한바퀴 끝나면 시간+1
    time+=1
	
    #두면이상 공기랑 닿으면, 빈칸 처리
    for i in range(n):
        for j in range(m):
            if visited[i][j]>=2:
                board[i][j]=0

    # 공기 카운트
    block_cnt=0
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                block_cnt+=1
    #탐색 한번 하고 난 그래프의 공기수가 배열의 크기랑 같으면 break
    if block_cnt==(n*m):
        break
    

print(time)