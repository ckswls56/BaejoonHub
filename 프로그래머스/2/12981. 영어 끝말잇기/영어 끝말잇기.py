
def solution(n, words):
    
    map=dict()
    i = 0
    before = ''
    for word in words:
        
        if before !=  '' and (word[:1] != before or map.get(word) != None):
            return i%n+1,i//n+1
        
        before = word[-1:]
        map[word] = True
        i+=1
    

    return 0,0