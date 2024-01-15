from itertools import combinations, product

def add_one(n):
    return n + 1

def count_case(list_a, list_b):
    count = 0
    index_b = 0
    
    for elem_a in list_a:
        while index_b < len(list_b) and list_b[index_b] < elem_a:
            index_b += 1
        count += index_b
    
    return count

def solution(dice):
    indices=list(range(len(dice)))
    combo_indices = list(combinations(indices, len(indices)//2))
    
    combo = list(combinations(dice, len(dice)//2))
    
    res = [
        sorted([sum(r) for r in product(*c)])
        for c in combo
    ]
    max_win = 0
    for i in range(len(res)//2):
        win = count_case(res[i],res[len(res)-i-1])
        if win>max_win:
            max_win=win
            ret = i
    
    #2개인 경우 
    if len(res)//2 == 1 and max_win < 18:
        ret+=1
        
    
    result = []        
    for c in combo_indices[ret] :
        result.append(c+1)
    
    return result
