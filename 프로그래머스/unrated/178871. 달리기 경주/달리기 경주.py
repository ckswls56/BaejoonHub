def solution(players, callings):
    
    map = {}
    
    for i in range(len(players)):
        map[players[i]] = i
    
    for c in callings :
        idx = map[c]
        
        map[c] = idx-1
        map[players[idx-1]] = idx
        
        temp = players[idx]
        players[idx] = players[idx-1]
        players[idx-1] = temp
        
    return players