number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

def solution(n, t, m, p):
    new_num = number[:n]
    new_num_arr = ['0']

    for i in range(1, m * t):
        temp = ''
        num = i
        while num > 0:
            num, mod = divmod(num, n)
            temp += new_num[mod]
        new_num_arr.append(temp[::-1])

    answer = "".join(new_num_arr)[p - 1::m][:t]

    return answer
