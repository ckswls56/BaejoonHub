from itertools import product
def solution(N, number):
    dp=[[] for i in range(8)]
    
    for i in range(8):
        dp[i].append(int(str(N)*(i+1)))
        
    
    for i in range(1,8):
        for j in range(i):
            for k in range(i):
                if j+1 + k+1 == i+1 :
                    for p in product(dp[j],dp[k]):
                        dp[i].append(p[0]+p[1])
                        dp[i].append(p[0]-p[1])
                        dp[i].append(p[0]*p[1])
                        if p[1] != 0 :
                            dp[i].append(p[0]//p[1])
                    
                               
    
    for i,d in enumerate(dp):
        
        for item in d:
            if item == number:
                return i+1
    
    return -1