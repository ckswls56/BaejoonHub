def solution(n, times):
    answer = 0
    times.sort()
    l = 1
    r = times[-1] * n
    
    while l+1< r:
        mid = (l + r) // 2
        total_processed = 0
        for t in times:
            total_processed += mid // t
        
        if total_processed >= n:
            r = mid
            answer = mid  # Update the answer when we find a feasible solution
        else:
            l = mid
        
    return answer
