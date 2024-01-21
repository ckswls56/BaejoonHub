def solution(str1, str2):
    answer = 0
    set1 = []
    set2 = []
    
    for i in range(len(str1)-1):
        temp = str1[i:i+2]
        if temp.isalpha():
            set1.append(temp.upper())
    
    for i in range(len(str2)-1):
        temp = str2[i:i+2]
        if temp.isalpha():
            set2.append(temp.upper())
            
    temp_set1 = set1[:]
    union = set1[:]
    intersection = []
    
    for s2 in set2:
        if s2 not in temp_set1:
            union.append(s2)
        else :
            temp_set1.remove(s2)
    
    for s2 in set2:
        if s2 in set1:
            set1.remove(s2)
            intersection.append(s2)
    
    
    if len(union)==0 and len(intersection) == 0 :
        return 65536
    
    answer = (int(len(intersection)/(len(union))*65536))        
            
    
    
            
    return answer