from collections import deque


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def left(arr):
    new_list = [[0]*n for _ in range(n)]
    q=deque()
    for i in range(n):
        idx = 0
        for j in range(n):
            if arr[i][j]:
                q.append(arr[i][j])
                
        
        while q :
            if len(q)>1 and q[0] == q[1] :
                q.popleft()
                q.appendleft(q.popleft()*2)
            new_list[i][idx] = q.popleft()
            idx += 1
    
    return new_list

def right(arr):
    new_list = [[0]*n for _ in range(n)]
    q=deque()
    for i in range(n):
        idx = n-1
        for j in range(n-1,-1,-1):
            if arr[i][j]:
                q.append(arr[i][j])
                
        
        while q :
            if len(q)>1 and q[0] == q[1] :
                q.popleft()
                q.appendleft(q.popleft()*2)
            new_list[i][idx] = q.popleft()
            idx -= 1
    
    return new_list

def up(arr):
    new_list = [[0]*n for _ in range(n)]
    q=deque()
    for j in range(n):
        idx = 0
        for i in range(n):
            if arr[i][j]:
                q.append(arr[i][j])
                
        
        while q :
            if len(q)>1 and q[0] == q[1] :
                q.popleft()
                q.appendleft(q.popleft()*2)
            new_list[idx][j] = q.popleft()
            idx += 1
    
    return new_list

def down(arr):
    new_list = [[0]*n for _ in range(n)]
    q=deque()
    for j in range(n):
        idx = n - 1
        for i in range(n-1,-1,-1):
            if arr[i][j]:
                q.append(arr[i][j])
                
        
        while q :
            if len(q)>1 and q[0] == q[1] :
                q.popleft()
                q.appendleft(q.popleft()*2)
            new_list[idx][j] = q.popleft()
            idx -= 1
    
    return new_list

def dfs(arr,cnt):
    if cnt == 5 :
        return max(map(max,arr))
    ret = - 1

    ret = max(ret,dfs(left(arr),cnt + 1))
    ret = max(ret,dfs(right(arr),cnt + 1))
    ret = max(ret,dfs(up(arr),cnt + 1))
    ret = max(ret,dfs(down(arr),cnt + 1))

    return ret


print(dfs(arr,0))