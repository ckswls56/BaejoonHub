def dfs(t):
    
    if len(t) < len(S):
        return 0
    
    if len(t) == len(S):
        
        return 1 if t==S else 0
    
    if t[-1] == 'A' and  dfs(t[:-1]) == 1:
        return 1
    
    if t[0] == 'B' and dfs(t[1:][::-1]) == 1:
        return 1
    
    return 0


S = input()
T = input()


print(dfs(T))