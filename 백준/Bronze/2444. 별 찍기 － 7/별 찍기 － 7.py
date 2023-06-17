def printSpace(n):
    while n > 0:
        print(" ", end="")
        n -= 1


def printStar(n):
    while n > 0:
        print("*", end="")
        n -= 1


n = int(input())

for i in range(n-1, 0, -1):
    printSpace(i)
    printStar(2*(n-i)-1)
    print()

printStar(n*2-1)

for i in range(1, n, 1):
    print()
    printSpace(i)
    printStar(2*(n-i)-1)
