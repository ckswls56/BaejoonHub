def solution(A, B):
    answer = 0
    
    B.sort()
    
    for a in A :
        low,high = 0,len(B)-1
        while low < high:
            mid = (low+high)//2
            if B[mid] <= a :
                low = mid + 1
            elif B[mid] > a:
                high = mid
        
        if B[high]>a:
            answer += 1
            del B[high]
    
    
    return answer