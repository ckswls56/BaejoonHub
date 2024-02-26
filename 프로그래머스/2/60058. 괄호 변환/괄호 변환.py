def check_cnt(s):
    return s.count('(') == s.count(')')

def check_correct(string):
    stack = list()
    
    for s in string:
        if s == '(':
            stack.append('(')
        elif stack :
            stack.pop()
        else :
            return False
        
    if stack :
        return False
    else:
        return True
                

def remove_end_reverse(s):
    s = s[1:len(s)-1]
    ret = []
    for i in s:
        if i =='(':
            ret.append(')')
        else:
            ret.append('(')
    
    return "".join(ret)
        
    
    
    

def sol(s):
    if s == '':
        return s
    u,v = '',''
    for i in range(0,len(s)-1,2):
        if check_cnt(s[:i+2]):
            u,v = s[:i+2],s[i+2:]
            break
            
    #u가 "올바른 괄호 문자열"
    if check_correct(u):
        u += sol(v)
        return u
    #4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  # 4-3. ')'를 다시 붙입니다. 
  # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  # 4-5. 생성된 문자열을 반환합니다.
    else :
        return '('+sol(v)+')'+remove_end_reverse(u)
        
        
        
    

def solution(p):
    answer = ''
    if check_correct(p):
        answer = p
    else :
        answer = sol(p)
    
    
    return answer