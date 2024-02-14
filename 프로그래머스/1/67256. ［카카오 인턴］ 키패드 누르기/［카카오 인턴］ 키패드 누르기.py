def solution(numbers, hand):
    answer = ''
    l_pos ,r_pos = (4,1),(4,3)
    for n in numbers:
        if n in [1,4,7]:
            answer+='L'
            if n == 1:
                l_pos = (1,1)
            elif n == 4:
                l_pos = (2,1)
            else :
                l_pos = (3,1)
        elif n in [3,6,9]:
            answer+='R'
            if n == 3:
                r_pos = (1,3)
            elif n == 6:
                r_pos = (2,3)
            else :
                r_pos = (3,3)
        else :
            if n == 2:
                l = abs(l_pos[0]-1)+abs(l_pos[1]-2)
                r = abs(r_pos[0]-1)+abs(r_pos[1]-2)
                if l < r:
                    answer += 'L'
                    l_pos = (1,2)
                elif l > r :
                    answer += 'R'
                    r_pos = (1,2)
                else:
                    if hand == 'left':
                        answer += 'L'
                        l_pos = (1,2)
                    else :
                        answer += 'R'
                        r_pos = (1,2)
            elif n == 5:
                l = abs(l_pos[0]-2)+abs(l_pos[1]-2)
                r = abs(r_pos[0]-2)+abs(r_pos[1]-2)
                if l < r:
                    answer += 'L'
                    l_pos = (2,2)
                elif l > r :
                    answer += 'R'
                    r_pos = (2,2)
                else:
                    if hand == 'left':
                        answer += 'L'
                        l_pos = (2,2)
                    else :
                        answer += 'R'
                        r_pos = (2,2)
            elif n == 8:
                l = abs(l_pos[0]-3)+abs(l_pos[1]-2)
                r = abs(r_pos[0]-3)+abs(r_pos[1]-2)
                if l < r:
                    answer += 'L'
                    l_pos = (3,2)
                elif l > r :
                    answer += 'R'
                    r_pos = (3,2)
                else:
                    if hand == 'left':
                        answer += 'L'
                        l_pos = (3,2)
                    else :
                        answer += 'R'
                        r_pos = (3,2)
            else :
                l = abs(l_pos[0]-4)+abs(l_pos[1]-2)
                r = abs(r_pos[0]-4)+abs(r_pos[1]-2)
                if l < r:
                    answer += 'L'
                    l_pos = (4,2)
                elif l > r :
                    answer += 'R'
                    r_pos = (4,2)
                else:
                    if hand == 'left':
                        answer += 'L'
                        l_pos = (4,2)
                    else :
                        answer += 'R'
                        r_pos = (4,2)
                
            
    return answer