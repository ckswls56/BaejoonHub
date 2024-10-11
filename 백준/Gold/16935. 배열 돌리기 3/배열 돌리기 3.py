import sys


n, m, r = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

command = list(map(int, sys.stdin.readline().split()))
for c in command:
    if c == 1:
        #상하 반전
        for i in range(n//2):
            arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    elif c == 2:
        #좌우 반전
        for j in range(m//2):
            for i in range(n):
                arr[i][j],arr[i][m-j-1] = arr[i][m-j-1],arr[i][j]
    elif c == 3:
        #오른쪽으로 90도
        arr = list(map(list,zip(*arr[::-1])))
        n,m = m,n
    elif c == 4:
        #왼쪽으로 90도
        arr = list(map(list,zip(*arr)))[::-1]
        n,m = m,n
    elif c == 5:
        # 4분할 후 오른쪽으로 이동
        for i in range(n//2):
            for j in range(m//2):
                arr[i][j],    arr[i+n//2][j],    arr[i][j+m//2],  arr[i+n//2][j+m//2] = arr[i+n//2][j],   arr[i+n//2][j+m//2],  arr[i][j],  arr[i][j+m//2]
    elif c == 6:
            # 4분할 후 왼쪽으로 이동
            for i in range(n//2):
                for j in range(m//2):
                    arr[i][j],    arr[i+n//2][j],    arr[i][j+m//2],  arr[i+n//2][j+m//2] = arr[i][j+m//2],arr[i][j],arr[i+n//2][j+m//2],arr[i+n//2][j]
                
                
        
for a in arr:
    print(*a)