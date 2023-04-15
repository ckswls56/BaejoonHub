map = {'ChongChong':1}

n = int(input())

for i in range(n):
    a,b = input().split()

    if(a not in map):
        map[a]=0
    if(b not in map):
        map[b]=0

    if(map[a]==1 or map[b]==1) :
        map[a]=1
        map[b]=1
        
cnt = 0
for i in map :
    if map[i]==1:
        cnt +=1

print(cnt)