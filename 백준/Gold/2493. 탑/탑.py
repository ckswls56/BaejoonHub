n = int(input())
arr = list(map(int, input().split()))

high_stack = []
ans = []

for i, item in enumerate(arr):
    # 현재 탑의 높이보다 작은 탑들은 stack에서 제거
    while high_stack and arr[high_stack[-1]] <= item:
        high_stack.pop()
        
    
    if not high_stack:
        ans.append(0)
    else:
        ans.append(high_stack[-1] + 1)
    
    
    high_stack.append(i)

print(*ans)
