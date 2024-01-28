import math
def solution(fees, records):
    answer = []
    m = {}
    sol={}
    for r in records:
        t,n,inout = r.split()
        if n in m :
            if inout == 'OUT':
                hour, minute = map(int, t.split(":"))
                b_hour,b_minute = map(int,m[n][0].split(":"))
                if int(minute)-int(b_minute) < 0 :
                    res =(int(hour)-int(b_hour) - 1) * 60 + int(minute)-int(b_minute) + 60
                else :
                    res =(int(hour)-int(b_hour)) * 60 + int(minute)-int(b_minute)
            
                sol[n] = sol.get(n,0) + res
            m[n] = (t,inout)
          
        else :
            m[n] = (t,inout)
    
    
    for n,item in m.items():
        if item[1] == 'IN':
            hour, minute = 23,59
            b_hour,b_minute = map(int,m[n][0].split(":"))
            if int(minute)-int(b_minute) < 0 :
                res =(int(hour)-int(b_hour) - 1) * 60 + int(minute)-int(b_minute) + 60
            else :
                res =(int(hour)-int(b_hour)) * 60 + int(minute)-int(b_minute)
            
            sol[n] = sol.get(n,0) + res

    for s in sorted(sol.items()):
        
        if s[1] <= fees[0] :
            answer.append(fees[1])
        else :
            answer.append(fees[1]+(math.ceil((s[1]-fees[0])/fees[2]))*fees[3])
    
    
    return answer