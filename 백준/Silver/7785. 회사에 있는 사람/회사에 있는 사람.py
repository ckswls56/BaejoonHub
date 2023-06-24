n = int(input())

map = {}
res = []
for i in range(n):
    str = input().split()
    map[str[0]] = str[1]

for i in map:
    if(map[i] == "enter"):
        res.append(i)

res.sort(reverse=True)

for i in res :
    print(i)
