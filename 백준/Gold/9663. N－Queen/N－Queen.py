def check(y,x):
    for i in range(y):
        if board[i] == x or abs(y-i)==abs(x-board[i]):
            return False
    
    return True

def dfs(y,n):
    if y==n:
        return 1
    ret = 0

    for i in range(n):
        if check(y,i):
            board[y]=i
            ret += dfs(y+1,n)
            board[y]=0

    return ret

n=int(input())
board = [0]*n
print(dfs(0,n))