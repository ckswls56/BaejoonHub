
s = list(input())

zero = True if s[0] == '0' else False

ans = 0
cnt = 0

for a in s[1:]:
    if zero and a == '0':
        continue
    elif not zero and a =='1':
        continue
    else:
        cnt += 1
        if cnt == 2:
            cnt = 0
            ans += 1
        
        zero = not zero

if cnt:
    ans += 1
    
print(ans)