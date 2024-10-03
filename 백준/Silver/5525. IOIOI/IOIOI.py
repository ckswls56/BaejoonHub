import sys

n = int(input())  # PN에서 N 값
m = int(input())  # 문자열 S의 길이
s = sys.stdin.readline().rstrip()  # 문자열 S

i = 0
ans = 0
count = 0

while i < m - 1:
    # 'IOI' 패턴을 발견했을 때
    if s[i:i+3] == 'IOI':
        count += 1
        i += 2  # IOI 패턴이므로 2칸 건너뜀

        # PN 패턴인지 확인
        if count == n:
            ans += 1
            count -= 1  # 중첩된 경우를 위해 카운트 감소
    else:
        i += 1
        count = 0  # 패턴이 끊겼으므로 count 리셋

print(ans)
