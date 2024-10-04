def solution(mats, park):
    
    mats.sort(reverse = True)
    
    
    for m in mats:
    
        for i in range(len(park)):
            for j in range(len(park[i])):
                if i+m <= len(park) and j+m <= len(park[i]):
                    flag = True

                    for k in range(i,i+m):
                        for l in range(j,j+m):
                            
                            if park[k][l] != '-1':
                                flag = False
                                break
                                
                        if not flag :
                            break
                    
                    if flag:
                        return m
    
    return -1