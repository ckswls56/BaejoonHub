import sys
rooms = []
p,m = map(int,input().split())

for _ in range(p):
    l,n = sys.stdin.readline().rstrip().split()
    l = int(l)
    for i in range(len(rooms)):
        if  rooms[i][0][0]-10<=l <= rooms[i][0][0]+10 and len(rooms[i]) < m:
            rooms[i].append((l,n))
            break
    else:
        rooms.append(([(l,n)]))


for room in rooms:
    room.sort(key = lambda x:x[1])
    if len(room) == m:
        print("Started!")
        for r in room:
            print(*r)
    else:
        print("Waiting!")
        for r in room:
            print(*r)