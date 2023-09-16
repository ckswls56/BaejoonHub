def solution(strArr):
    answer = 0
    map = {}
    for i in range(1,31):
        map[i] = 0
        
    for str in strArr:
        map[len(str)] += 1
    
    return max(map.values())