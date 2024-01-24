import heapq as h

def solution(scoville, K):
    h.heapify(scoville)
    
    
    answer = 0
    while scoville[0] < K :
        m1 = h.heappop(scoville)
        m2 = h.heappop(scoville)
        h.heappush(scoville,m1+m2*2)
        if len(scoville) == 1 and scoville[0] < K :
            return -1
        answer += 1
        
    
    
    return answer