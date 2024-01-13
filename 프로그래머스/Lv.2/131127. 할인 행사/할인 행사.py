def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)):
        part = discount[i:10+i]
     
        answer+=1
        for j in range(len(number)):
            if(part.count(want[j])<number[j]):
                answer-=1
                break
            
        
    return answer