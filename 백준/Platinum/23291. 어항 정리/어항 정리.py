

def get_diff(arr):
    mins=min(arr)
    maxs=max(arr)
    return maxs-mins

def fish_move():
    x,y = len(bowl[0]),len(bowl)
    temp = [([0]*x) for _ in range(y)]

    for i in range(y):
        for j in range(x):
            fish = bowl[i][j]
            if  fish == -1:
                continue

            for dy,dx in direction:
                ny,nx = i+dy,j+dx
                if 0<=ny<y and 0<=nx<x:
                    near_fish = bowl[ny][nx]
                    if near_fish == -1:
                        continue
                    d = (fish - near_fish)//5
                    if d <= 0:
                        continue

                    temp[ny][nx] += d
                    temp[i][j] -= d
    
    for i in range(y):
        for j in range(x):
            bowl[i][j] += temp[i][j]

def bowl_merge():
    res = []
    x,y = len(bowl[0]),len(bowl)
    for i in range(y):
        for j in range(x):
            if bowl[i][j] != -1:
                res.append(bowl[i][j])
    
    return res

                    

                    



direction = [(-1,0),(1,0),(0,-1),(0,1)]
n,k = map(int,input().split())
fishes = list(map(int,input().split()))
bowl = [[fish] for fish in fishes]
ans = 0

while True :

    maxs = 0
    mins = 10001

    for i in range(n):
        mins = min(bowl[i][0],mins)
        maxs = max(bowl[i][0],maxs)

    if maxs-mins <= k:
        break
    ans += 1

    for i in range(n):
        if bowl[i][0]==mins:
            bowl[i][0]+=1

    #첫번쨰 어항 공중부양
    bowl[1].extend(bowl.pop(0))

    while True:
        idx = 0
        while len(bowl[idx])>=2:
            idx+=1
            if len(bowl) - idx < len(bowl[0]):
                break
        
        #남은 어항 길이보다 높이가 크면 종료
        if len(bowl) - idx < len(bowl[0]):
            break

        cur_bowl  = []
        for _ in range(idx):
            cur_bowl.append(bowl.pop(0))
        
        rotate_bwol = list(map(list,zip(*cur_bowl[::-1])))
        for i in range(len(rotate_bwol)):
            bowl[i].extend(rotate_bwol[i])
        
        height = len(bowl[0])

    for i in range(len(bowl)):
        while len(bowl[i])<height:
            bowl[i].append(-1)
        
        

    fish_move()
    bowl = bowl_merge()

    flag = False
    for _ in range(2):
        idx = len(bowl)//2
        temp = []

        while idx:
            temp.append(bowl.pop(0))
            idx-=1
        
        if not flag :
            bowl = [[bo] for bo in bowl]

            for i in range(len(bowl)):
                bowl[i].append(temp.pop())
            flag = True
        else :
            temp_180 = [t[::-1] for t in temp[::-1]]
            for i in range(len(bowl)):
                bowl[i].extend(temp_180[i])

    fish_move()
    bowl = bowl_merge()
    bowl = [[bo] for bo in bowl]

print(ans)