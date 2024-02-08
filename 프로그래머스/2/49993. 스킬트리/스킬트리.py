def solution(skill, skill_trees):
    answer = 0
    m = {}
    for i in range(ord('A'),ord('Z')+1):
        m[chr(i)]  = -1
        
    for i,s in enumerate(skill):
        m[s] = i
    
    for skill_tree in skill_trees:
        idx = 0
        for s in skill_tree:
            
            if m[s] == -1:
                continue
            elif m[s] == idx:
                idx +=1
            else :
                answer -= 1
                break
        
        answer += 1
        
    
    return answer