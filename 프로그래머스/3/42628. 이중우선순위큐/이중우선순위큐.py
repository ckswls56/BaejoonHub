import heapq as h
def solution(operations):
    answer = []
    minh = []
    maxh = []
    for op in operations:
        
        if op == 'D 1':
            if minh:
                x = h.heappop(maxh)[1]
                minh.remove(x)
        elif op == 'D -1':
            if minh:
                x = h.heappop(minh)
                maxh.remove((-x,x))
        else :
            h.heappush(minh,int(op.split()[1]))
            h.heappush(maxh,(-int(op.split()[1]),int(op.split()[1])))
        
    
    if minh:
        return (h.heappop(maxh)[1],h.heappop(minh))
    else :
        return [0,0]