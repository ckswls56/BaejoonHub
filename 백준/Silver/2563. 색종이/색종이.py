arr = [[0 for _ in range(100)] for _ in range(100)]


def paste(x, y):
    for i in range(10):
        for j in range(10):
            arr[i+y][x+j] = 1


def sol():
    sum = 0
    for i in range(100):
        for j in range(100):
            if(arr[i][j]):
                sum += 1
    return sum


n = int(input())

while(n):
    x, y = map(int, input().split())
    paste(x, y)
    n -= 1

print(sol())
