def solution(topping):
    answer = 0
    a=[0] * len(topping)
    m = {}
    for i,t in enumerate(topping):
        if m.get(t,0) == 0:
            m[t] = 1
            a[i] = len(m)
        else:
            m[t] += 1
            a[i] = a[i-1]
    
    b= [len(m)] * len(topping)
    
    for i,t in enumerate(topping):
        if m.get(t,1) == 1:
            b[i] = b[i-1]-1
        else:
            m[t] -= 1
            b[i] = b[i-1]
    

    for x,y in zip(a,b):
        if x==y :
            answer += 1
      
        
    return answer