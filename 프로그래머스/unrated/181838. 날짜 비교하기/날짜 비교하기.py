def comp(a,b):
    if a<b:
        return 1
    elif a>b:
        return 0
    else :
        return -1


def solution(date1, date2):
    if comp(date1[0],date2[0]) == 1 :
        return 1
    elif comp(date1[0],date2[0]) == 0 :
        return 0
    else :
        if comp(date1[1],date2[1]) == 1 :
            return 1
        elif comp(date1[1],date2[1]) == 0 :
            return 0
        else :
            if comp(date1[2],date2[2]) == 1 :
                return 1
            elif comp(date1[2],date2[2]) == 0 :
                return 0
            else :
                return 0
            
        
    