n = int(input())
arr = []
for i in range(n):
    name,d,m,y = map(str,input().split())
    arr.append((name,int(d),int(m),int(y)))

arr.sort(key = lambda x : (x[3],x[2],x[1]))
print(arr[-1][0])
print(arr[0][0])