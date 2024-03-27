from itertools import permutations

def check(a,b,strike,ball):
    c_s,c_b = 0,0
    for x,y in zip(a,b):
        if x==y:
            c_s += 1
    
    for i in range(len(a)):
        for j in range(len(b)):
            if i!=j:
                if a[i]==b[j]:
                    c_b +=1
    
    if c_s == strike and c_b == ball:
        return True
    else :
        return False

ans = [[]for _ in range(3)]
number = [str(i) for i in range(1,10)]

n = int(input())
arr = []
for _ in range(n):
    n,s,b = map(int,input().split())
    arr.append((n,s,b))
possible = []
for p in permutations(number,3):
    x = ''.join(p)
    for n,s,b in arr:
        if not check(str(x),str(n),s,b):
            break
    else :
        possible.append(p)

print(len(possible))