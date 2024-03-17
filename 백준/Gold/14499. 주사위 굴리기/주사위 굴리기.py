import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dice = [0] * 6
commands = list(map(int, input().split()))
for c in commands:
    flag = False
    if c == 1:  # 동쪽
        if y + 1 < m:
            y += 1
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
            flag = True
    elif c == 2:  # 서쪽
        if y - 1 >= 0:
            y -= 1
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
            flag = True
    elif c == 3:  # 북쪽
        if x - 1 >= 0:
            x -= 1
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
            flag = True
    elif c == 4:  # 남쪽
        if x + 1 < n:
            x += 1
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
            flag = True
    
    if flag :
        if maps[x][y] == 0:
            maps[x][y] = dice[5]
        else:
            dice[5] = maps[x][y]
            maps[x][y] = 0
        print(dice[0])


