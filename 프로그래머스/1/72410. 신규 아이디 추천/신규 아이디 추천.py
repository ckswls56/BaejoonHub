def solution(new_id):
    
    str2=''
    for s in new_id.lower():
        if s.isalpha() or s.isnumeric() or s =='-' or s=='_' or s=='.':
            str2+=s
    
    before = str2[0]
    str3 =''
    for s in str2[1:]:
        if before != '.':
            str3+=before
            before = s
        else :
            if s =='.':
                before = s
            else :
                str3+=before
                before = s
    if str2[-1] != '.':
        str3 += str2[-1]
    
    
    str4 = ''
    if str3:
        if str3[0] =='.' and str3[-1] =='.':
            str4 = str3[1:len(str3)-1]
        elif str3[0] == '.':
            str4 = str3[1:]
        elif str3[-1] == '.':
            str4 = str3[:len(str3)-1]
        else :
            str4 = str3
    str5 = ''
    
    if str4 == '':
        str5 ='a'
    else :
        str5 = str4
    
    str6 = str5
    
    if len(str5)>=16:
        str6 = str5[:15]
        if str6[-1] == '.':
            str6 = str6[:14]
    
    if len(str6) <= 2:
        while len(str6) < 3:
            str6 += str6[-1]
            
           
    return str6