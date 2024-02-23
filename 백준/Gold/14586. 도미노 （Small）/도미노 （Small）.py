import heapq as h
def get_maxdirection(start):
    left,right = 0,0
    length = sum(arr[start])
    for next_x in range(start+1,n):
        if not visited[next_x] and length >= arr[next_x][0]:
            right += 1
            length = max(length,sum(arr[next_x]))
        else:
            break

    length = arr[start][0]-arr[start][1]
    for next_x in range(start-1,-1,-1):
        if not visited[next_x] and length <= arr[next_x][0]:
            left += 1
            length = min(length,arr[next_x][0]-arr[next_x][1])
        else:
            break
    if left > right :
        return (left,"left")
    else:
        return (right,"right")
        


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
visited = [False] * n
heap = []

for i in range(n):
    res = get_maxdirection(i)
    h.heappush(heap,(-res[0],i,res[1]))

answer = 0
while not all(visited):
    answer += 1
    distance,x,direction = h.heappop(heap)
    distance = -distance
    heap = []
    if direction == "left":
        for i in range(x-distance,x+1):
            visited[i] = True
    else:
        for i in range(x,x+distance+1):
            visited[i] = True

    for i in range(n):
        if not visited[i]:
            res = get_maxdirection(i)
            h.heappush(heap,(-res[0],i,res[1]))

print(answer)
