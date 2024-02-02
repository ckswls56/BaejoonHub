direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(dirs):
    answer = 0
    visit = set()
    
    y, x =0,0
    
    for d in dirs:
        if d == 'U':
            dy, dx = y + direction[0][0], x + direction[0][1]
        elif d == 'D':
            dy, dx = y + direction[1][0], x + direction[1][1]
        elif d == 'L':
            dy, dx = y + direction[2][0], x + direction[2][1]
        else:
            dy, dx = y + direction[3][0], x + direction[3][1]
        
        if -5 <= dy <= 5 and -5 <= dx <= 5:
            go = (y,x,dy,dx)
            back = (dy,dx,y,x)
            y,x = dy,dx
            
            if go not in visit :
                visit.add(go)
                visit.add(back)
                answer += 1
               
        
    return answer
