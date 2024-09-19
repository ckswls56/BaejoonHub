def sol(arr):
    
    sum = 0
    
    for x in arr:
        sum += int(x)
        
    
    return str(sum)




start = input()

ans = 0


while int(start)>9:
    start = sol(start)
    ans += 1
    
print(ans)
if int(start) % 3 == 0:
    print("YES")
else:
    print("NO")