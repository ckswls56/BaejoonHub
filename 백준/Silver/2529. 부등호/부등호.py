from itertools import permutations

k = int(input())
operand = input().split()

l = list(range(10))

mins,maxs = '999999999','000000000'

for p in permutations(l,k+1):
    
    for i in range(k):
        op = operand[i]
        
        if op == '<':
            if p[i] >= p[i+1]:
                break
        elif op == '>':
            if p[i] <= p[i+1]:
                break
    else:
        temp = ''
        for x in p:
            temp += str(x)
        
        mins,maxs = min(mins,temp),max(maxs,temp)
        
print(maxs)
print(mins)