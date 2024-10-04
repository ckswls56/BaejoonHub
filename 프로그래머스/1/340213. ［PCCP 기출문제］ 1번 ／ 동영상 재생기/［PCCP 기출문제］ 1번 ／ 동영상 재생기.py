def get_time(t):
    m,s = map(int,t.split(':'))
    return m*60 + s

def get_time_str(t):
    
    first = '0'
    second = '0'
    
    if len(str(t//60))==1:
        first+= str(t//60)
    else :
        first = str(t//60)
        
    if len(str(t%60))==1:
        second+= str(t%60)
    else :
        second = str(t%60)
        
    
    return first+':'+second

def solution(video_len, pos, op_start, op_end, commands):
    
    current = get_time(pos)
    
    op_st,op_et = get_time(op_start),get_time(op_end)
    end_time = get_time(video_len)
  

    for c in commands:
        if op_st<=current<=op_et:
                current = op_et
    
        if c == 'next':
            current += 10
            current = min(current,end_time)
        else :
            current -= 10
            current = max(current,0)
            
        
    
    if op_st<=current<=op_et:
            current = op_et
            
    
    
    answer = get_time_str(current)
    
    
    return answer