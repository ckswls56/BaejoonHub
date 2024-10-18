s  = list(input())

#슬라이딩 윈도우 크기
window_size = s.count('a')
#원형처리
s += s[0:window_size]

ans = 987654321

for i in range(len(s)-(window_size)):
    ans = min(ans,s[i:i+window_size].count('b'))

print(ans)