from collections import deque

def rotation(arr,dir):
    if dir == 1:
        arr.appendleft(arr.pop())
    else :
        arr.append(arr.popleft())
    


def sol(n,dir):
    if n == 1:
        if wheel[0][2] != wheel[1][-2]:
            if wheel[1][2] != wheel[2][-2]:
                if wheel[2][2] != wheel[3][-2]:
                    rotation(wheel[3],-dir)
                rotation(wheel[2],dir)        
            rotation(wheel[1],-dir)
        rotation(wheel[0],dir)
    elif n == 2:
        if wheel[1][2] != wheel[2][-2]:
            if wheel[2][2] != wheel[3][-2]:
                rotation(wheel[3],dir)
            rotation(wheel[2],-dir)        
        if wheel[1][-2] != wheel[0][2]:
            rotation(wheel[0],-dir)    
        rotation(wheel[1],dir)
    elif n == 3:
        if wheel[2][-2] != wheel[1][2]:
            if wheel[1][-2] != wheel[0][2]:
                rotation(wheel[0],dir)
            rotation(wheel[1],-dir)        
        if wheel[2][2] != wheel[3][-2]:
            rotation(wheel[3],-dir)    
        rotation(wheel[2],dir)
    else :
        if wheel[3][-2] != wheel[2][2]:            
            if wheel[2][-2] != wheel[1][2]:
                if wheel[1][-2] != wheel[0][2]:
                    rotation(wheel[0],-dir)
                rotation(wheel[1],dir)        
            rotation(wheel[2],-dir)
        rotation(wheel[3],dir)            

def score():
    ans = 0
    if wheel[0][0] == 1:
        ans += 1
    if wheel[1][0] == 1:
        ans += 2
    if wheel[2][0] == 1:
        ans += 4
    if wheel[3][0] == 1:
        ans += 8

    return ans


wheel=[]

for _ in range(4):
    temp = deque()
    for s in input():
        temp.append(int(s))
    wheel.append(temp)

k = int(input())
for i in range(k):
    n,dir = map(int,input().split())
    sol(n,dir)

print(score())