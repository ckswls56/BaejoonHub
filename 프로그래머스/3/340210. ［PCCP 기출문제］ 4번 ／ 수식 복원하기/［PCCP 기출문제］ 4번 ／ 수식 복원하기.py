def TenToN(n, num):
    if num == 0:
        return "0"

    answer = ""
    while num:
        num, mod = divmod(num, n)
        answer = str(mod) + answer

    return answer

def cal(a, op, b):
    if op == '+':
        return a + b
    else:
        return a - b

def solution(expressions):
    answer, answer_format = [], []
    max_format, hint = 0, []

    for e in expressions:
        num1, func, num2, _, ans = e.split(" ")

        # Finding the maximum base required
        for idx in range(len(num1)):
            max_format = max(max_format, int(num1[idx]))
        for idx in range(len(num2)):
            max_format = max(max_format, int(num2[idx]))

        if ans != "X":  # Known results
            hint.append(e)
            for idx in range(len(ans)):
                max_format = max(max_format, int(ans[idx]))
        else:  # Unknown results
            answer.append(e)

    for n in range(max_format + 1, 10):  # Checking possible bases
        check = True
        for h in hint:
            num1, func, num2, _, ans = h.split(" ")
            num1, num2, ans = int(num1,n), int(num2,n), int(ans,n)

            if (func == '+') and (num1 + num2 != ans): 
                check = False
                break
            if (func == '-') and (num1 - num2 != ans): 
                check = False
                break

        if check:  # Valid base
            answer_format.append(n)

    for idx in range(len(answer)):
        num1, func, num2, _, ans = answer[idx].split(" ")
        ans_set = set()

        for a in answer_format:
            num_1, num_2 = int(num1,a), int(num2,a)

            if func == "+":
                ans_set.add(str(TenToN(a, num_1 + num_2)))
            if func == "-":
                ans_set.add(str(TenToN(a, num_1 - num_2)))

        if len(ans_set) == 1:  # Single valid answer
            answer[idx] = answer[idx].replace('X',list(ans_set)[0])
        else:  # Multiple possible answers
            answer[idx] = answer[idx].replace('X','?')

    return answer
