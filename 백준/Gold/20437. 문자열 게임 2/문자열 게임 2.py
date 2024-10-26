import sys
from collections import defaultdict

t=int(sys.stdin.readline())

for _ in range(t): #테스트 케이스 수만큼 반복.
    w=sys.stdin.readline().rstrip()
    k=int(sys.stdin.readline())
    
    d = defaultdict(list)
    
    for i in range(len(w)):
        if w.count(w[i]) >= k:
            d[w[i]].append(i)
            
    
    if not d:
        print(-1)
    else:
        short,long = 10000,1
        
        for char in d:
            for i in range(len(d[char])-k+1):
                length = d[char][i+k-1] - d[char][i] + 1
                
                short,long = min(short,length),max(long,length)
                
                
        print(short,long)