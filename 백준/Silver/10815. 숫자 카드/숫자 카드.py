n = int(input())

arr = list(map(int,input().split()))

card = {}

for i in arr :
    card[i] = True



m = int(input())

check = list(map(int,input().split()))

for c in check :
    if card.setdefault(c) != None:
        print(1,end=" ")
    else :
        print(0,end=" ")
