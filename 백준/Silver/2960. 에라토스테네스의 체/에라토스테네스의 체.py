n,k = map(int,input().split())

arr = [i for i in range(2,n+1)]

cnt = 0

while(len(arr)):
    m = min(arr)
    for i in arr :
        if i % m == 0:
            arr.remove(i)
            cnt +=1
            if cnt == k:
                print(i)
                break
