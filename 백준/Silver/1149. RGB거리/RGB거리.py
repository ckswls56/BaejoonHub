n = int(input())
arr_red = [0]*n
arr_green = [0]*n
arr_blue = [0]*n
i = 0
while i < n:
    r,g,b = map(int,input().split())
    arr_red[i] = r
    arr_green[i] = g
    arr_blue[i] = b
    i+=1

dp_red = [0]*n
dp_green = [0]*n
dp_blue = [0]*n

dp_red[0] = arr_red[0]
dp_green[0] = arr_green[0]
dp_blue[0] = arr_blue[0]

for i in range(1,n):
    dp_red[i] = arr_red[i] + min(dp_green[i-1],dp_blue[i-1])
    dp_green[i] = arr_green[i] + min(dp_red[i-1],dp_blue[i-1])
    dp_blue[i] = arr_blue[i] + min(dp_red[i-1],dp_green[i-1])

print(min(dp_red[n-1],dp_green[n-1],dp_blue[n-1]))