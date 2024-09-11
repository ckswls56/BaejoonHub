import heapq as h

dir = [(-1,0),(1,0),(0,-1),(0,1)]

def sol(s):
    
    pq = []
    
    t = 0
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 :
                h.heappush(pq,(t,arr[i][j],i,j))
                
    
    while pq :
        
        t,k,y,x = h.heappop(pq)
        
        if t>= s :
            break

        for dy,dx in dir:
            cy,cx = dy+y,dx+x
            if 0<=cy<n and 0<=cx<n and arr[cy][cx] == 0:
                h.heappush(pq,(t+1,k,cy,cx))
                arr[cy][cx] = k
    
                
                
        

n,k = map(int,input().split())

# s초 뒤에 x,y에 존재하는 바이러스 번호

arr = []

for _ in range(n):
    arr.append(list(map(int,input().split())))
    

s,x,y = map(int,input().split())

sol(s)
print(arr[x-1][y-1])