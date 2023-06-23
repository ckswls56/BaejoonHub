arr = []


def sum_of_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
            arr.append(i)
    return sum


while True:
    n = int(input())
    if n == -1:
        break
    if n == sum_of_divisors(n):
        print(n, "=", end=" ")
        for i, num in enumerate(arr):
            print(num, end="")
            if i < len(arr) - 1:
                print(" + ", end="")
        print()
    else:
        print(n, "is NOT perfect.")
    arr.clear()
