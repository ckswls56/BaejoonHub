
def sol(y,x,n):
    if n == 1:
        star[y][x] = '*'
        return
    
    
    
    for i in range(n):
        star[i+y][x] = '*'
        star[y][i+x] = '*'
        star[y+n-1][i+x] = '*'
        star[i+y][x+n-1] = '*'
    
    sol(y+2,x+2,n-4)
    
        


n = int(input())

star = [[' ']*500 for _ in range(500)]

sol(0,0,(n-1)*4 + 1)

for i in range((n-1)*4 + 1):
    for j in range((n-1)*4 + 1):
        print(star[i][j],end="")
    print()