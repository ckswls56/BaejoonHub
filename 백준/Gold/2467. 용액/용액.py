n = int(input())
arr = list(map(int,input().split()))

arr.sort()

# two pointer
l,r = 0,n-1
ans = 2000000000
ans_l,ans_r = -1,-1
while l<r:
    if ans > abs(arr[l]+arr[r]):
        ans = abs(arr[l]+arr[r])
        ans_l,ans_r = arr[l],arr[r]
        
    
    if l+1 == r:
        break
    
    if abs(arr[l+1] + arr[r])<abs(arr[l]+arr[r-1]):
        l+=1
    else:
        r-=1
    
print(ans_l,ans_r)