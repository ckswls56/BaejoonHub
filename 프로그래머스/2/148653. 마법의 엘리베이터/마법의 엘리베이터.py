def solution(storey):
    answer = 0
    
    while storey > 0:
        storey, rem = divmod(storey, 10)
        
        ## 더하는게 이득
        if rem > 5 or (rem == 5 and storey % 10 >= 5):
            answer += (10 - rem)
            storey += 1
        ##빼는게 이득
        else:
            answer += rem
        
    return answer