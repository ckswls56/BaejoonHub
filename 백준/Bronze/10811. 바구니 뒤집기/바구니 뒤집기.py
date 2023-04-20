def swap_range(arr, start, end):
    # 시작 인덱스와 끝 인덱스의 범위가 리스트 인덱스를 벗어나는 경우
    if start >= len(arr) or end >= len(arr):
        print("Index out of range!")
        return arr
    
    # 범위의 시작 인덱스와 끝 인덱스가 바뀐 경우
    if start > end:
        start, end = end, start
    
    # 범위 내 원소를 바꿈
    for i in range((end - start + 1) // 2):
        arr[start + i], arr[end - i] = arr[end - i], arr[start + i]
    
    return arr



n,m = map(int,input().split())

arr = [i+1 for i in range(n)]

for a in range(m) :
    i,j = map(int,input().split())
    swap_range(arr,i-1,j-1)
    
print(*arr)