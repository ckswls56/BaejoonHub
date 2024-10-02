
s = int(input())
i = 1

while s > 0 :
    s-=i
    i+=1
    
if s == 0:
    i+=1

print(i-2)
    