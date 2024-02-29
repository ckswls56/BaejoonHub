import math

def get_symmetry(l,r,n):
    
    while l>=0 and r < n :
        if arr[l] == arr[r]:
            l-=1
            r+=1
        else :
            break
    return (l+1,r-1)

s_n = int(input())
arr = list(map(int,input().split()))
p_n = int(input())
for i in range(p_n):
    gender,switch = map(int,input().split())
    if gender == 1:
        #man
        for j in range(switch-1,s_n,switch):
            arr[j] = abs(arr[j]-1)
    else :
        l,r = get_symmetry(switch-2,switch,s_n)
        
        for j in range(l,r+1):
            
            arr[j] = abs(arr[j]-1)
            
            
for i in range(math.ceil(s_n/20)):
    print(*arr[i*20:(i+1)*20])

