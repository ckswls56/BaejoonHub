def count_open_windows(n):
    windows = [False] * n  # n개의 창문을 False로 초기화
    for person in range(1, n+1):
        for window in range(person, n+1, person):
            windows[window-1] = not windows[window-1]  # 창문을 열거나 닫음

    return windows.count(True)  # 열려 있는 창문의 개수 반환


n = int(input())

cnt = 1
sum = 3
plus = 5
while(n > sum):
    sum += plus
    cnt += 1
    plus += 2

print(cnt)