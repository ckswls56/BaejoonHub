def rotate(n,y,x):
    if n == 0:
        return y,x
    elif n == 1:
        return -x,y
    elif n ==2:
        return y,-x
    else :
        return x,y

n = int(input())

a = [list(map(int,input().split())) for _ in range(n)]
ratio = [(0,-2,0.05),(-1,-1,0.1),(1,-1,0.1),(-1,0,0.07),(1,0,0.07),
         (2,0,0.02),(-2,0,0.02),(1,1,0.01),(-1,1,0.01)]
direction = [(0,-1),(1,0),(0,1),(-1,0)]


y,x = n//2,n//2

step = 1
cnt = 0
flag = False
d = 0
ans = 0

while not (y==0 and x==0):
    cnt+=1
    y+=direction[d][0]
    x+=direction[d][1]
    temp = 0
    #비율 구하기
    
    for dy,dx,r in ratio:
        dy,dx = rotate(d,dy,dx)
        ny,nx = y+dy,x+dx
        if 0<=ny<n and 0<=nx<n:
            a[ny][nx]+= int(a[y][x]*r)
            temp += int(a[y][x]*r)
        else :
            ans += int(a[y][x]*r)
            temp += int(a[y][x]*r)
    # a 구하기
    dy,dx = rotate(d,0,-1)
    if 0<=y+dy<n and 0<=x+dx < n :
        a[y+dy][x+dx] += a[y][x] - temp 
    else :
        ans += a[y][x] - temp 
    a[y][x] = 0

    if cnt == step :
        if not flag:
            flag = True
        else :
            step += 1
            flag = False
        d= (d+1) % 4
        cnt = 0

print(ans)