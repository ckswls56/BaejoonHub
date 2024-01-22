def count(h,m,s):
    h_d,m_d,s_d = (h*30+m*0.5+s*0.5/60)%360,(m*6+s*0.1)%360,s*6
    res = -1
   
    if(s_d>=m_d):
        res+=1
    if(s_d>=h_d):
        res+=1
        
    res += (h*60+m)*2 ## 초침은 분당 분침과 시침과 1번씩 겹치게 되있다.
    res -= h ## 그러나 59분 -> 00 분은 시침 안겹친다 24
    if h>=12 : res -= 2 ## 11시 -> 12시
    
    return res


def solution(h1, m1, s1, h2, m2, s2):
    
    
    
    
    ## 00시 0분 0초 에서 시작하거나 12시 0분 0초에서 시작할 떄는 1번 처리
    answer = count(h2,m2,s2)-count(h1,m1,s1)
    if (m1 == 0 and s1 == 0) and (h1 == 0 or h1 == 12):
        answer +=1


    return answer