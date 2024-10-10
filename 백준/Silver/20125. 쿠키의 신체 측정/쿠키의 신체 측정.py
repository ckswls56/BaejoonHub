
def get_length(y,x,dy,dx):
    ret = 0
    while is_cookie(y,x):
        ret+=1
        y,x = y+dy,x+dx
        if not (0<=y<n and 0<=x<n):
            break
    
    return ret


def is_cookie(y,x):
    if arr[y][x] == '*':
        return True
    else:
        return False

n = int(input())

arr = [list(input()) for _ in range(n)]

h_y,h_x = -1,-1

flag = False


# 머리 위치 찾기
for i in range(n):
    for j in range(n):
        if is_cookie(i,j):
            h_i,h_j = i,j
            flag = True
            break
    if flag:
        break
    
j = h_j
for i in range(h_i,n):
    if is_cookie(i-1,j) and is_cookie(i,j) and is_cookie(i,j-1) and is_cookie(i,j+1) and is_cookie(i+1,j):
        h_y,h_x = i,j
        break
        
left_arm = get_length(h_y,h_x-1,0,-1)
right_arm = get_length(h_y,h_x+1,0,1)
backborn = get_length(h_y+1,h_x,1,0)
left_leg = get_length(h_y+backborn+1,h_x-1,1,0)
right_leg = get_length(h_y+backborn+1,h_x+1,1,0)



print(h_y+1,h_x+1)
print(left_arm,right_arm,backborn,left_leg,right_leg)
