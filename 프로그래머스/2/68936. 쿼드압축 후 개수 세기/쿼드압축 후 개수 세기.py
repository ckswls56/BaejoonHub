def devide(x,y,n,arr):
    
    if n == 1:
        if arr[y][x] == 0:
            return (1,0)
        else:
            return (0,1)
    
    zero = 0
    one = 0
    
    for i in range(y,y+n,n//2):
        for j in range(x,x+n,n//2):
            res = devide(j,i,n//2,arr)
            zero += res[0]
            one += res[1]

    if zero == 0 :
        return (0,1)
    elif one == 0:
        return (1,0)
    else:
        return (zero,one)
            
        
        
    


def solution(arr):
    answer = devide(0,0,len(arr),arr)
    return answer