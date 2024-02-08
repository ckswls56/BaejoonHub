def solution(record):
    answer = []
    m = {}
    l = []
    for r in record:
        if r.startswith('Leave'):
            op,uid = r.split()
            l.append((op,uid))
        else :
            op,uid,name = r.split()
            m[uid] = name
            if op =='Enter':
                l.append((op,uid))
    
    for op,uid in l:
        if op == 'Enter':
            answer.append(m[uid]+'님이 들어왔습니다.')
        else :
            answer.append(m[uid]+'님이 나갔습니다.')
            
        
    
    return answer