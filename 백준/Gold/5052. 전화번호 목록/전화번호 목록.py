# greedy 하게
import sys

t = int(input())

while t:
    t-=1
    
    n = int(input())
    
    numbers = [sys.stdin.readline().rstrip()  for _ in range(n)]
    
    numbers.sort()
    flag = True
    for i in range(n-1):
        length = len(numbers[i])
        
        if numbers[i] == numbers[i+1][:length]:
            flag = False
            break
        
    
    if flag:
        print('YES')
    else:
        print("NO")