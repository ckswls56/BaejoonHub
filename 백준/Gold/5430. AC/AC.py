from collections import deque

T = int(input())

for _ in range(T):
    command = input().strip()
    
    n = int(input().strip())
    
    if n == 0:
        input()  # 빈 배열 입력 처리
        arr = deque()
    else:
        strings = input().strip()[1:-1]
        arr = deque(strings.split(',')) if strings else deque()
    
    is_reversed = False  # R이 등장하면 reverse 대신 방향을 바꿈
    error_flag = False
    
    for c in command:
        if c == 'R':
            is_reversed = not is_reversed
        else:
            if not arr:
                print('error')
                error_flag = True
                break
            if is_reversed:
                arr.pop()
            else:
                arr.popleft()
    
    if not error_flag:
        if is_reversed:
            arr.reverse()
        
        # 출력 포맷 처리
        print(f"[{','.join(arr)}]")

