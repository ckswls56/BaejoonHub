def solution(n):
    num = ['1','2','4']
    
    answer = ''
    
    while n > 0:
        n,m = divmod(n-1,3)
        answer += num[m]
        
    
    
    return answer[::-1]