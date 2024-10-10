import sys
S = sys.stdin.readline().strip()
n = 0
while len(S):
    n += 1 # 1씩 증가
    num = str(n)
    while len(num) and len(S): #둘 다 아직 숫자가 있고
        if num[0] == S[0]: #만약 n의 앞자리가 S의 앞자리랑 같으면
            S = S[1:] # 문자열 이동
        num = num[1:] # 앞자리 이동
print(n)