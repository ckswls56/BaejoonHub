from collections import deque

def bfs():

    q = deque()
    q.append((array,0))
    while q:
        arr,cnt = q.popleft()

        if arr == ans:
            return cnt
        for i in range(n-k+1):
            temp = arr[i:i+k]
            temp.reverse()
            temp = arr[:i] + temp + arr[i+k:]
            if "".join(temp) not in visited:
                visited.add("".join(temp))
                q.append((temp,cnt+1))
    return -1
            


n,k = map(int, input().split())
array = list(input().split())
visited = set("".join(array))
ans = sorted(array)
if array == ans:
    print(0)
else:
    print(bfs())
