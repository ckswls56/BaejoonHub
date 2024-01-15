from collections import deque

def dfs(k,dungeons,depth):
    ret = depth
    for i in range(len(dungeons)):
        if k>=dungeons[i][0]:
            new_list = dungeons[:i] + dungeons[i+1:]
            ret=max(ret,dfs(k-dungeons[i][1],new_list,depth+1))
    
    return ret
            

    

def solution(k, dungeons):
    answer = dfs(k,dungeons,0)
    
    return answer