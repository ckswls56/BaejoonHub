S = list(input())
T = list(input())
flag = False

while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
    if S == T :
        flag = True
        break

if flag:
    print(1)
else:
    print(0)
