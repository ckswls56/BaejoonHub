import sys

N = int(sys.stdin.readline())
cal = list(sys.stdin.readline().strip())

def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    elif op == '-':
        return a - b

def dfs(index, value):
    if index == N - 1:
        return value

    max_value = -1 * 2**31

    if index + 2 < N:
        # 다음번에 나오는 수와 계산하는데, 다음번에 나오는 수가 괄호가 쳐져있지 않을 때
        next_value = calculate(value, cal[index + 1], int(cal[index + 2]))
        max_value = max(max_value, dfs(index + 2, next_value))

    if index + 4 < N:
        # 다음번에 나오는 수와 계산하는데, 다음번에 나오는 수가 다다음번에 나오는 수와 괄호가 쳐져있을 때
        next_next_value = calculate(int(cal[index + 2]), cal[index + 3], int(cal[index + 4]))
        next_value = calculate(value, cal[index + 1], next_next_value)
        max_value = max(max_value, dfs(index + 4, next_value))

    return max_value


print(dfs(0, int(cal[0])))