k = int(input())


x = 1

while k :
    k-=1
    arr = list(map(int,input().split()))
    arr = arr[1:]
    print("Class",x)
    
    maxs = max(arr)
    mins = min(arr)
    arr.sort()
    
    gap = 0
    for i in range(1,len(arr)):
        gap = max(gap,arr[i]-arr[i-1])
        
    
    print("Max ",maxs,", Min ",mins,", Largest gap ",gap,sep="")
    x+=1