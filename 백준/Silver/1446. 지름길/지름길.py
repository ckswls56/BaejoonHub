def dfs(start,total,visited):
    if len(visited) == n:
        return total+(d-start)
    ret = total + (d-start)
    for s,e,c in arr:
        if (s,e,c) not in visited:
            if start <= s and e<=d:
                visited.add((s,e,c))
                ret = min(ret,dfs(e,(s-start)+total+c,visited))
                visited.remove((s,e,c))
    
    return ret

n,d = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

print(dfs(0,0,set()))