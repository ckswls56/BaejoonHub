
def solution(name):
    #연속되는 A가 있을 때, 그것의 왼쪽이나 오른쪽부터 시작하며 알파벳을 변경하는 것이 가장 효율적이다.
    
    answer = 0
    min_move = len(name)-1
    for i,char in enumerate(name):
        
        answer += min(ord(char)-ord('A'),ord('Z')-ord(char)+1)
        next = i+1
        
        while next < len(name) and name[next]=='A':
            next+=1
            
        min_move = min(min_move,2*i+len(name)-next,i+(len(name)-next)*2)
        
    
    return answer + min_move
