def solution(money):
    if len(money) == 3:
        return max(money)
    
    dp1=[]
    dp2=[]
    
    dp1.append(money[0])
    dp1.append(money[1])
    dp1.append(money[0]+money[2])
    
    dp2.append(money[1])
    dp2.append(money[2])
    dp2.append(money[1]+money[3])
    
    for i in range(3,len(money)-1):
        if dp1[i-3]>dp1[i-2]:
            dp1.append(dp1[i-3]+money[i])
        else :
            dp1.append(dp1[i-2]+money[i])
    
    for i in range(4,len(money)):
        if dp2[i-4]>dp2[i-3]:
            dp2.append(dp2[i-4]+money[i])
        else :
            dp2.append(dp2[i-3]+money[i])
            
    
        
    
    answer = max(dp1[-1],dp1[-2],dp2[-1],dp2[-2])
    return answer