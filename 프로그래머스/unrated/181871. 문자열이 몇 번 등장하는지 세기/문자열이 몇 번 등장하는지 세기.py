def solution(myString, pat):
    answer = 0
    l = list(myString)
    for i in range(len(l)):
        if l[i] == pat[0]:
            if ''.join(l[i:i+len(pat)]) == pat:
                answer+=1
                
    return answer