import heapq as h
#max heap

def check(heap,a):
    ans = 0
    for h in heap:
        if -h > a :
            ans+=1
    return ans

p = int(input())


for i in range(1,p+1):
    heap = []
    arr = list(map(int,input().split()))
    
    h.heappush(heap,-arr[1])
    
    ans = 0
    
    for a in arr[2:]:
        
        if -heap[0] < a :
            h.heappush(heap,-a)
        else :
            ans += check(heap,a) 
            h.heappush(heap,-a)
        
            
    
    print(i,ans)