# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

def like_near(s):
    like_list = like[s]

    res = (0,0,-1,-1)
    
    for i in range(n):
        for j in range(n):
            if class_room[i][j] != -1:
                continue
            like_cnt = 0
            blank_cnt = 0

            for dy,dx in direction:
                ny,nx = i+dy,j+dx
                if 0<=ny<n and 0<=nx<n:
                    seat = class_room[ny][nx]
                    if seat == -1:
                        blank_cnt+=1
                    elif seat in like_list:
                        like_cnt += 1

            if like_cnt>res[0]:
                res = (like_cnt,blank_cnt,i,j)
                
            elif like_cnt == res[0]:
                if blank_cnt>res[1]:
                    res = (like_cnt,blank_cnt,i,j)

            if res[2] == -1 and res[3] == -1:
                res = (0,0,i,j)
    
    return (res[2],res[3])



ans = 0
n = int(input())
direction = [(-1,0),(1,0),(0,-1),(0,1)]
like = [ [] for _ in range((n**2)+1)]
order = []
for _ in range(n**2):
    s,x1,x2,x3,x4 = map(int,input().split())
    like[s].append(x1)
    like[s].append(x2)
    like[s].append(x3)
    like[s].append(x4)
    order.append(s)

class_room = [[-1 for _ in range(n)]for _ in range(n)]

for s in order :
    y,x = like_near(s)
    class_room[y][x] = s
    


for i in range(n):
    for j in range(n):
        like_list = like[class_room[i][j]]
        
        cnt = 0
        for dy,dx in direction:
            ny,nx = i+dy,j+dx
            
            if 0<=ny<n and 0<=nx<n :
                friend = class_room[ny][nx]

                if friend in like_list:
                    cnt += 1
        
        ans += int(10**(cnt-1))

print(ans)