# X축으로 이동하면서 왼쪽 오른쪽에 있는 가장 큰 벽을 탐색하는데 
# 자기 기준으로 왼쪽 오른쪽에 큰벽이 무조건 존재해야하고
# 큰벽들 중 작은벽을 기준으로 물이 고이게 된다.

def check_left(x):
    ret = 0
    
    for i in range(x-1,-1,-1):
        if blocks[i]>blocks[x]:
            ret = max(ret,blocks[i]-blocks[x])
                
    return ret

def check_right(x):
    ret = 0
    
    for i in range(x,w):
        if blocks[i]>blocks[x]:
            ret = max(ret,blocks[i]-blocks[x])
                
    return ret


h,w = map(int,input().split())
blocks = list(map(int,input().split()))

res = 0

for i in range(len(blocks)):
    left = check_left(i)
    if left :
        right = check_right(i)
        
        res += min(left,right)
        
print(res)