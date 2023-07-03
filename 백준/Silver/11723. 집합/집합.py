import sys
arr = [False] * 20

m = int(input())

while(m):
    m-=1
    string = sys.stdin.readline().rstrip().split()
    op = string[0]
    if string[0] != "all" and string[0] != "empty" :
        x = int(string[1])

    if op == "add" :
        arr[x-1] = True
    elif op == "remove" :
        arr[x-1] = False
    elif op == "check" :
        if arr[x-1] == True :
            print(1)
        else :
            print(0)
    elif op == "toggle" :
        arr[x-1] = not arr[x-1]
    elif op =="all":
        for i in range(20):
            arr[i]= True
    else :
        for i in range(20):
            arr[i] = False