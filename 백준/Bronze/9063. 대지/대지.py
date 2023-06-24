n = int(input())

x, y = map(int, input().split())
min_x = x
max_x = x
min_y = y
max_y = y

while(n-1 > 0):
    x, y = map(int, input().split())
    if(x < min_x):
        min_x = x
    if(x > max_x):
        max_x = x
    if(y < min_y):
        min_y = y
    if(y > max_y):
        max_y = y

    n -= 1

print((max_x-min_x)*(max_y-min_y))
