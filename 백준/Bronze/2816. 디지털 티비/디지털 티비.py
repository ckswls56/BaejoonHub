
n = int(input())

a = [input() for _  in range(n)]

i = 0 

f1,f2 = False,False

answer = ''

while True:
    if a[0] == 'KBS1':
        break
    
    if a[i] == 'KBS1':
        answer+='4'
        a[i],a[i-1] = a[i-1], a[i]
        i -=1
    else:
        answer+='1'
        i+=1
        



while True:
    if a[1] == 'KBS2':
        break
    
    if a[i] == 'KBS2':
        answer+='4'
        a[i],a[i-1] = a[i-1], a[i]
        i -=1
    else:
        answer+='1'
        i+=1


print(answer)