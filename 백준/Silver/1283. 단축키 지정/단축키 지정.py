
n = int(input())

sets = set()
answer = []
words = []
for _ in range(n):
    option = input().split()
    words.append(option)
    flag = False
    # 1
    for i in range(len(option)):
        
        if option[i][0].lower() not in sets:
            sets.add(option[i][0].lower())
            answer.append((i,0))
            flag = True
            break
    # 2
    if flag :
        continue
    flag = False
    for i in range(len(option)):
        if flag:
            break
        for j in range(len(option[i])):
            if option[i][j].lower() not in sets:
                sets.add(option[i][j].lower())
                answer.append((i,j))
                flag=True
                break 
    
    if not flag:
        answer.append((-1,-1))



for i in range(len(words)):
    a,b = answer[i]
    if a == -1 and b == -1:
        print(*words[i])
        continue
    for j in range(len(words[i])):
        for k in range(len(words[i][j])):
            if j==a and b ==k:
                print('['+words[i][j][k]+']',end="")
            else:
                print(words[i][j][k],end="")
        print(" ",end="")
    print()