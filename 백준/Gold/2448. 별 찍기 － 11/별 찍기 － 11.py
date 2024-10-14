def sol(y,x,n):
    if n == 3:
        
        b[y][x] = '*'
        b[y+1][x+1] = b[y+1][x-1] = '*'
        for i in range(x-2,x+3):
            b[y+2][i] = '*'
    
    else :
        next_n = n//2
        sol(y,x,next_n)
        sol(y+next_n,x+next_n,next_n)
        sol(y+next_n,x-next_n,next_n)
        
            

n = int(input())

b = [[' ']*(n*2) for _ in range(n)]

# 맨위, 중앙에서 시작
sol(0,n-1,n)

for line in b:
    print("".join(line))
