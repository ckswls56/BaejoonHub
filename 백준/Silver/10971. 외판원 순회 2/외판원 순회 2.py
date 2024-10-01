
def sol(arr,y,s):
    
    if len(arr) == n :
        return s+ cost[y][start] if cost[y][start] > 0 else 10000000  # 출발점으로 돌아갈 수 없는 경우 처리
    
    ret = 10000000
    
    for i in range(n):
        if i not in arr and cost[y][i]>0:
            arr.add(i)
            ret = min(ret,sol(arr,i,s+cost[y][i]))
            arr.remove(i)
    
    return ret


n = int(input())

cost = [list(map(int,input().split())) for _ in range(n)]


ans = 10000000
for i in range(n):
    start=i
    ans = min(ans,sol(set({i}),i,0))
    
print(ans)