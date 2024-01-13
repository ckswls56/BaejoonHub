def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for c in citations:
        cnt = 0
        for i in range(len(citations)):
            if c <= citations[i]:
                cnt+=1
        print(cnt,c)
                
        if answer<min(cnt,c):
            answer = min(cnt,c)
    
    return answer
        
    