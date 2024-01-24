import heapq as h
def solution(jobs):

    answer,now,i =0,0,0
    start = -1
    heap = []
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                h.heappush(heap,[j[1],j[0]])
        if heap :
                current = h.heappop(heap)
                start = now
                now += current[0]
                answer += (now - current[1])
                i+=1
        else :
                now += 1


    return answer//len(jobs)