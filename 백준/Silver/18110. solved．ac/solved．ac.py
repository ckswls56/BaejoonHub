def convert(x):
    if len(str(x))>=3:
        for i in range(len(str(x))):
            if str(x)[i] == '.':
                if int(str(x)[i+1]) >= 5 :
                    return int(x)+1
                else:
                    return int(x)
    
    return int(x)

n = int(input())

if n == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(n)]
    minus = convert(n*0.15)
    arr.sort()
    length = len(arr)
    arr = arr[minus:length-minus]
    print(convert(sum(arr)/len(arr)))