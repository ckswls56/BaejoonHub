def solution(genres, plays):
    answer = []
    one_m = {}
    two_m = {}
    
    for i in range(len(plays)):
        temp = one_m.get(genres[i],[])
        temp.append(i)
        one_m[genres[i]]= temp
        two_m[genres[i]] =two_m.get(genres[i],0) + plays[i]
    
    
    l = sorted(one_m.items(),key = lambda x : two_m[x[0]],reverse = True)
    
    
    for song,i in l:
        new_l = sorted(i,key = lambda x : (-plays[x],x))
        
        for a in new_l[:2]:
            answer.append(a)
        
    
    
    return answer