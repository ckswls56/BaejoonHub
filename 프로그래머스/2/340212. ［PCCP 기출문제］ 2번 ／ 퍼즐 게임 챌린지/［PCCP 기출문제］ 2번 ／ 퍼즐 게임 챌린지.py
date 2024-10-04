def solution(diffs, times, limit):
    l,r  = 1, 100001
    
    while l<r:
        mid = (l+r)//2
        total = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid:
                total += times[i]
            else:
                total += (times[i-1]+times[i])*(diffs[i]-mid) + times[i]
        
        if total <= limit :
            r = mid
        else :
            l = mid + 1
    
    return r