
board=[[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
       ,[10,13,16,19],[20,22,24],[30,28,27,26],[25,30,35,40,0]]



# dfs 상황에서 각각의 말을 움직여 보고 최대가 되게 한다.
# 첫번쨰 인자는 좌표 두번쨰 인자는 경로
horse = [(-1,0),(-1,0),(-1,0),(-1,0)]

command = list(map(int,input().split()))

def dfs(horse,depth,total):
    if depth == 10 :
        return total
    
    ret = total

    # 4개의 말에 대하여
    for i in range(4):
        pos,route_idx = horse[i]
        next_pos = pos + command[depth]
        next_route_idx = route_idx
        # flag = False
        if route_idx == 0:
            if (next_pos+1) == 5:
                next_route_idx = 1
                next_pos = 0
            elif (next_pos+1) == 10:
                next_route_idx = 2
                next_pos = 0
            elif (next_pos+1) == 15:
                next_route_idx = 3
                next_pos = 0
            elif (next_pos+1) == 20:
                next_route_idx = 4
                next_pos = 3
            elif (next_pos+1) > 20:
                next_route_idx = 4
                next_pos = 4 # end

        elif route_idx == 1 or route_idx == 3:
            if next_pos >= 4:
                next_route_idx = 4
                next_pos = next_pos - 4
        elif route_idx == 2:
            if next_pos >= 3:
                next_route_idx = 4
                next_pos = next_pos - 3
        elif route_idx == 4:
            if next_pos >= 4:
                next_pos = 4
        
        for j in range(4):
            if i!=j and (next_pos,next_route_idx) == horse[j] and horse[j] != (4,4):
                break
        else :
            next_cost = board[next_route_idx][next_pos]
            horse[i] = (next_pos, next_route_idx)
            ret = max(ret, dfs(horse, depth + 1, total+next_cost))
            horse[i] = (pos, route_idx)    



    return ret


print(dfs(horse,0,0))