n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(1)
else:
    inc_cnt = 1  # 증가하는 구간의 길이
    dec_cnt = 1  # 감소하는 구간의 길이
    ans = 1      # 가장 긴 구간의 길이

    for i in range(1, n):
        if arr[i] > arr[i-1]:  # 증가하는 경우
            inc_cnt += 1
            dec_cnt = 1  # 감소 카운터는 초기화
        elif arr[i] < arr[i-1]:  # 감소하는 경우
            dec_cnt += 1
            inc_cnt = 1  # 증가 카운터는 초기화
        else:  # 같은 값이 연속되는 경우
            inc_cnt += 1
            dec_cnt += 1

        ans = max(ans, inc_cnt, dec_cnt)  # 최대 구간 길이 업데이트

    print(ans)
