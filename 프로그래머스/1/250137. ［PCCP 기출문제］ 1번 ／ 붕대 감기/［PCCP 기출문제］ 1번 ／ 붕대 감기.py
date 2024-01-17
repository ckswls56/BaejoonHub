def solution(bandage, health, attacks):
    max_health = health
    
    for i in range(len(attacks)-1):
        health -= attacks[i][1]
        
        if health <= 0 :
            return -1
        
        
        for j in range(1,attacks[i+1][0]-attacks[i][0]):
            health += bandage[1]
            if j % bandage[0] == 0 :
                health += bandage[2]
            if health > max_health:
                health = max_health
            
    health -= attacks[-1][1]
    if health <= 0 :
        return -1
    return health