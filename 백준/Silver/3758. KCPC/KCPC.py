import sys
T = int(input())

for _ in range(T):
    
    #팀 개수 , 문제 개수 , 팀 ID, 로그 개수
    n,k,t,m = map(int,sys.stdin.readline().rstrip().split())
    
    # total score , solved times , last solve
    score = [[0,0,0,i] for i in range(n+1)]
    s_m = {}
    t_m = {}
    solved_m = {}
    
    for time in range(m):
        #팀 ID, 문제번호 , 흭득한 점수
        i,j,s = map(int,sys.stdin.readline().rstrip().split())
        
        s_m[(i,j)] = max(s_m.get((i,j),0),s)
        t_m[i] = time
        solved_m[i] = solved_m.get(i,0) + 1
        
    
    for k,v in s_m.items():
        k = k[0]
        score[k][0],score[k][1],score[k][2] = score[k][0] + v, solved_m[k],t_m[k]
        
    
    score.sort(key=lambda x : (-x[0],x[1],x[2]))
    
    ans = 1
    
    for _,_,_,id in score:
        if id == t:
            print(ans)
        ans+=1