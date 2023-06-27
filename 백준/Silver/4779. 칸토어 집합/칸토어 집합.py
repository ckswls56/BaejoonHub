def cantore(str, n, times):
    if times == 0:
        return str
    res = ''
    res += str
    for i in range(n):
        res += ' '
    res += str
    return cantore(res, n*3, times-1)


n = int(input())
while (True):
    try:
        if n == 0:
            print('-')
        else:
            print(cantore('-', 1, n))
        n = int(input())
    except EOFError:
        break
