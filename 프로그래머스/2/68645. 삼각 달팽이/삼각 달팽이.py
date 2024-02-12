def solution(n):
    answer = [[] for _ in range(n)]
    num = 1
    i = 0
    j = 0
    l,h = 0,n-1
    
    # True 면 밑으로 -> i++
    down = True
    cnt = 0
    
    
    while num <= n*(n+1)//2:
        if (i == l and not down) or (i == h and down):
            temp = j
            while len(answer[i]) < i+1:
                answer[i].insert(temp,num)
                num += 1
                temp += 1
            if i == l and not down:
                l += 1
                i += 1
            elif i == h and down:
                h -= 1
                i -= 1
            down = not down
            cnt += 1
            
            if cnt % 2 == 0:
                j+=1
        
        if down :
            if len(answer[i])<i+1:
                answer[i].insert(j,num)
                num += 1    
            
            if i+1 <= h:
                i+=1
        else :
            
            if len(answer[i]) < i+1:
                if j == 0:
                    answer[i].append(num)
                else:
                    answer[i].insert(-j,num)
                num += 1
            if i-1 >= l:
                i-=1
        
            
    return sum(answer,[])