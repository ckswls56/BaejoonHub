def solution(t, p):
    answer = 0
    string = []
    for i in range(len(t)-len(p)+1):
        string.append(t[i:i+len(p)])

    for s in string :
        if int(s) <= int(p) :
            answer+=1
        
    return answer
