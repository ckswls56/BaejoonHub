coin = [25, 10, 5, 1]

t = int(input())

for i in range(t):
    c = int(input())
    for j in range(4):
        print(int(c/coin[j]), end=" ")
        c = c % coin[j]
    print()
