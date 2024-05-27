from collections import Counter

def check_palindrome(c):
    odd = 0
    for i in c.values():
        if i % 2 == 1:
            odd += 1
            if odd > 1:
                return False
    return True

c = Counter(input())
ans = ''

odd = sum(c.values()) % 2 == 1

if not check_palindrome(c):
    print("I'm Sorry Hansoo")
else :
    times = sum(c.values())//2
    for i in range(times):

        for j in sorted(c):
            if c[j] >= 2:
                ans += j
                c[j] -= 2
                break
        

    if odd:
        mid = c.most_common()[0][0]
        print(ans + mid + ans[::-1])
    else:
        print(ans + ans[::-1])