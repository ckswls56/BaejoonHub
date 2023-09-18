def solution(s):
    times = 0
    zeros = 0
    while s != '1':
        times += 1
        zeros += s.count('0')
        s = (''.join(c for c in s if  c != '0'))
        s=bin(len(s))[2:]
        
        
    answer=[times,zeros]
        
    return answer