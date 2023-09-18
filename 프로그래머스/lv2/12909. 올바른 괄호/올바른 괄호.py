def solution(s):
    answer = True
    if s.count('(') != s.count(')'):
        return False
    else :
        i=0
        q=list()
        while i<len(s):
            while i<len(s) and s[i] == '(':
                q.append(s[i])
                i+=1
            while i<len(s) and s[i] == ')' :
                if s[i] != ')':
                    return False
                else :
                    if len(q) == 0 and s[i] == ')':
                        return False
                    i+=1
                    q.pop()
            
            

        
    return True