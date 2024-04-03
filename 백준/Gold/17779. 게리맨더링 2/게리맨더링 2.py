import sys
N = int(sys.stdin.readline())
# pan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
pan = [[]]
for _ in range(N):
    pan.append([0] + list(map(int, sys.stdin.readline().split())))

def mancount(x,y,d1,d2):
    count = [0,0,0,0,0]
    # 경계구역 설정
    five = [[0]*(N+1)for _ in range(N+1)]

    for i in range(d1+1):
        five[x+i][y-i] = 1  #1
        five[x+i+d2][y+d2-i]=1  #3
    
    for i in range(d2+1):
        five[x+i][y+i] = 1  #2
        five[x+i+d1][y+i-d1] = 1 #4
    
    # 경계 안에 five 채우기
    
    for i in range(x+1,x+d1+d2):
        flag = False
        for j in range(1,N+1):
            if five[i][j] == 1:
                if flag:
                    flag = False
                else :
                    flag = True
            else :
                if flag:
                    five[i][j] = 1

    for i in range(1,N+1):
        for j in range(1,N+1):
            peoples = pan[i][j]
            if five[i][j] == 1:
                count[4] += peoples
            else :
                if i<x+d1 and j <= y:
                    count[0] += peoples
                elif i<=x+d2 and y < j:
                    count[1] += peoples
                elif x+d1<=i and j < y-d1+d2:
                    count[2] += peoples
                elif x+d2 < i and y-d1+d2 <= j :
                    count[3] += peoples

    return max(count) - min(count)

# 경계선 x,y,d1,d2를 정해야 함

# 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
# 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
# 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
# 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
# 5번 선거구: 그 외의 나머지 + 경계선
min_count = float('inf')
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if 1 <= x < x+d1+d2 <= N  and 1 <= y-d1 < y < y+d2 <= N:
                    min_count = min(min_count,mancount(x,y,d1,d2))

print(min_count)