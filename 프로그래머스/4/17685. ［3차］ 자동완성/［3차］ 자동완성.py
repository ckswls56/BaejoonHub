from collections import deque
def check(a,b):
    i = 0
    for x,y in zip(a,b):
        if x != y:
            
            return i+1
            
        i+=1
    return(len(a))+1

def solution(words):
    answer = 0
    words.sort()

    for i in range(len(words)):
        before,next = i-1,i+1
        a,b = 1,1
        if 0 <= before :
            a = check(words[before],words[i])
        if next < len(words):
            b = check(words[i],words[next])
        
        answer += min(max(a,b),len(words[i]))
    
    return answer
