
a = list(input())
b = input()
ans = 0
i = 0
while i < len(a):
    if a[i] == b[0]:
        j = 0
        while j < len(b):
            if i+j<len(a) and a[i+j] == b[j]:
                j+=1
            else:
                break
        
        if j == len(b):
            ans += 1
            i+=j-1
            
    i+= 1

print(ans)