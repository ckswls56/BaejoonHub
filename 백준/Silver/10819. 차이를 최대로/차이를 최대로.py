from itertools import permutations

def cal(arr):
    
    res = 0
    
    for i in range(len(arr)-1):
        res += abs(arr[i]-arr[i+1])
        
    return res

n = int(input())

arr = list(map(int,input().split()))

ans = 0

for combo in permutations(arr):
    
    ans = max(ans,cal(combo))

print(ans)