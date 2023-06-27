from collections import deque
queue = deque()
MAXSIZE = 100001
visited = [-1]*MAXSIZE


def bfs(n,k):
    cnt = 0
    visited[n] = 0
    
    queue.append(n)

    while(queue):
        c = queue.popleft()
        
        if c == k :
            cnt += 1
        
        for next in [c*2,c+1,c-1] :
            if 0 <= next < MAXSIZE :
                if visited[next] == -1 or visited[next]>= visited[c] + 1:
                    visited[next] = visited[c] + 1
                    queue.append(next)

    print(visited[k])
    print(cnt)

n,k = map(int,input().split())
bfs(n,k)
