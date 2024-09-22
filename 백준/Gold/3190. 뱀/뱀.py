
direction = [(0,1),(1,0),(0,-1),(-1,0)]

n= int(input())
k = int(input())
apples = []
for _ in range(k):
    y,x = map(int,input().split())
    apples.append((y,x))
    
l = int(input())
command = {}
for _ in range(l):
    x,c = input().split()
    x = int(x)
    command[x] = c
    
    
    


snake = []

snake.append((0,0))


d = 0

ny,nx = 1,1

t = 1

while snake:
    
    dy,dx = direction[d][0],direction[d][1]
    ny,nx = ny+dy,nx+dx
    
    if 1<=ny<=n and 1<=nx<=n and (ny,nx) not in snake:
        snake.append((ny,nx))
    else :
        break
    
    if (ny,nx) in apples:
        apples.remove((ny,nx))
    else:
        snake.pop(0)
    
    
    
    
    if command.get(t,-1) == 'L':
        d = (d-1) %4
    elif command.get(t,-1) == 'D':
        d = (d+1) %4
    t+=1
    
    
print(t)