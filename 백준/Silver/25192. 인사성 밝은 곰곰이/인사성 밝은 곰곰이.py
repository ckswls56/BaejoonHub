dict = {}

n = int(input())

sum = 0
for i in range(n):
    text = input()
    if text == "ENTER":
        sum += len(dict)
        dict.clear()
    else:
        dict[text] = True

sum += len(dict)
print(sum)