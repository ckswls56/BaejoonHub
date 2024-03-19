import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

# y,x
direction = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
cloud = []
#비바라기 시전
cloud.append((n-1,0))
cloud.append((n-1,1))
cloud.append((n-2,0))
cloud.append((n-2,1))

for i in range(m):
    d,s = map(int,input().split())

    dy,dx = direction[d-1]
    moved_cloud = []
    #구름 이동
    for cy,cx in cloud :
        ny,nx = (cy+dy*s)%n,(cx+dx*s)%n
        # print(cy+dy*s,cx+dx*s,ny,nx)
        a[ny][nx] += 1
        moved_cloud.append((ny,nx))

    for cy,cx in cloud :
        ny,nx = (cy+dy*s)%n,(cx+dx*s)%n
    # 대각선 체크
        for diy,dix in [(-1,-1),(-1,1),(1,1),(1,-1)]:
            y,x = ny+diy,nx+dix
        
            if 0<=y<n and 0<=x<n and a[y][x] > 0:
                a[ny][nx] += 1
                

    new_cloud = []
  
    for i in range(n):
        for j in range(n):
            if a[i][j] >= 2 and (i,j) not in moved_cloud:
                new_cloud.append((i,j))
                a[i][j]-=2
    
    cloud = new_cloud

print(sum(sum(row) for row in a))
