def solution(s):
    
    data=s[1:len(s)-1]
    
    sets_list = [set(map(int, s.strip("{}").split(','))) for s in data.split('},{')]
    sorted_sets = sorted(sets_list, key=len)
    
    result_set = set()
    result = []
    for i in sorted_sets:
        
        for j in str(i).strip("{}").replace(',','').split():
            if (int(j)) not in result_set:
                result.append(int(j))
                result_set.add(int(j))
    
    return result
