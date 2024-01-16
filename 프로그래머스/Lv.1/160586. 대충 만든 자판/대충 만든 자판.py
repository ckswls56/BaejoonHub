def solution(keymap, targets):
    answer = []
    m = {}
    for key in keymap:
        i = 1
        for k in key:
            if k not in m:
                m[k]=i
            elif m[k]>i:
                m[k]=i
            i+=1
    
    for target in targets:
        temp = 0
        for t in target:
            if t not in m:
                temp = -1
                break
            else:
                temp+= m[t]
        answer.append(temp)

    return answer