
def get_distance(y,x):
    i = 0
    res = []
    for dy,dx in direction:
        ny,nx = y+dy , x+dx
        cnt = 0
        while 0<=ny<n and 0<=nx<n:
            if arr[ny][nx] == 1:
                break
            else :
                ny,nx = ny+dy,nx+dx
            cnt += 1

        if ny == -1 or ny == n or nx == -1 or nx == n:
            res.append((cnt,i))
        i += 1


    return res




def dfs(depth,cells,total_wire):
    if depth == len(processor):
        return (cells,total_wire)

    ret = (cells,total_wire)
    y,x,possible = processor[depth]

    for distance,direct in possible:
        dy,dx = direction[direct][0],direction[direct][1]
        ny,nx = y+dy, x+dx
        while 0<=ny<n and 0<=nx<n:
            if arr[ny][nx] == 1:
                break
            else :
                ny,nx = ny+dy,nx+dx
        if ny == -1 or ny == n or nx == -1 or nx == n:
            ny,nx = y+dy, x+dx
            while 0 <= ny < n and 0 <= nx < n:
                arr[ny][nx] = 1
                ny, nx = ny + dy, nx + dx

            temp = dfs(depth+1,cells+1,total_wire+distance)
            ny, nx = y + dy, x + dx
            while 0 <= ny < n and 0 <= nx < n:
                arr[ny][nx] = 0
                ny, nx = ny + dy, nx + dx

            if temp[0]>ret[0]:
                ret = temp
            elif temp[0] == ret[0] and temp[1]<ret[1]:
                ret = temp
        else :
            temp = dfs(depth+1,cells,total_wire)
            if temp[0]>ret[0]:
                ret = temp
            elif temp[0] == ret[0] and temp[1]<ret[1]:
                ret = temp

    return ret





# 상 하 좌 우
direction = [(-1,0),(1,0),(0,-1),(0,1)]
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1,T+1):
    # ///////////////////////////////////////////////////////////////////////////////////

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    processor = []
    for i in range(1,n-1):
        for j in range(1,n-1):
            if arr[i][j] == 1:
                processor.append((i,j,get_distance(i,j)))

    iter = len(processor)
    ans = (0,999)
    for i in range(iter):
        temp = dfs(0,0,0)
        if temp[0] > ans[0]:
            ans = temp
        elif temp[0] == ans[0] and temp[1] < ans[1]:
            ans = temp
        processor.append(processor.pop(0))

    ans = ans[1]
    print('#'+str(test_case)+' '+str(ans))

    # ///////////////////////////////////////////////////////////////////////////////////

    # ///////////////////////////////////////////////////////////////////////////////////
