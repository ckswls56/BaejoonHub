def rotate(arr, x1, y1, x2, y2):
    stack = []

    for j in range(y1,y2+1):
        stack.append(arr[x1][j])
            
    for i in range(x1+1,x2+1):
            stack.append(arr[i][y2])
            
    for j in range(y2-1,y1-1,-1):
        stack.append(arr[x2][j])
            
    for i in range(x2-1,x1,-1):
            stack.append(arr[i][y1])
    
    ret = min(stack)
    
    for i in range(x1,x2+1):
        arr[i][y1] = stack.pop()
        
    for j in range(y1+1,y2+1):
        arr[x2][j] = stack.pop()
        
    for i in range(x2-1,x1,-1):
        arr[i][y2] = stack.pop()
    
    for j in range(y2,y1,-1):
        arr[x1][j] = stack.pop()
            

    
    return ret
    
    

    


def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns for _ in range(rows)]

    n = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = n
            n += 1

    for x1, y1, x2, y2 in queries:
        answer.append(rotate(arr, x1 - 1, y1 - 1, x2 - 1, y2 - 1))
    return answer