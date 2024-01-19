def solution(msg):
    answer = []
    d = {chr(ord('A') + i): i + 1 for i in range(26)}
    
    i = 0
    while i < len(msg):
        temp = msg[i]
        
        while temp in d:            
            i+=1
            w = temp
            if(i < len(msg)):
                temp += msg[i]
            else :
                break
            
        answer.append(d[w])
        
        last_number = list(d.values())[-1]
        d[temp] = last_number + 1

    return answer