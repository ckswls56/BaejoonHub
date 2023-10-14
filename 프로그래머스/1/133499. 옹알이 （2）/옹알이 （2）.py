def solution(babbling):
    sounds = ['aya','ye','woo','ma']
    answer = 0
    for i in range(len(babbling)):
        for sound in sounds:
            if  (sound in babbling[i]) and (sound*2 not in babbling[i]):
                babbling[i] = babbling[i].replace(sound,'!')
            
        if all(c == '!' for c in babbling[i]):
                answer+=1
    
    return answer