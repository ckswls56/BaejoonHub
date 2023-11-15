from collections import deque
def solution(queue1, queue2):
    q1,q2 = deque(queue1),deque(queue2)
    s1,s2 = sum(q1),sum(q2)
    count,limit = 0,len(q1)*3
    
    if s1==s2:
        return count
    
    else :
        while True :
            if s1>s2:
                x = q1.popleft()
                s1 -= x
                s2 += x
                q2.append(x)
                count+=1
            elif s1<s2:
                x = q2.popleft()
                s1 += x
                s2 -= x
                q1.append(x)
                count+=1
            else:
                return count
            
            if count == limit:
                return -1

    return count