import math

def solution(n, stations, w):
    answer = 0
    s_range = []
    
    # 각 기지국의 전파 범위를 저장합니다.
    for s in stations:
        s_range.append((s-w, s+w))
    
    i = 0
    l = 1
    
    # 첫 번째 기지국 이전 영역을 처리합니다.
    while i < len(stations):
        answer += math.ceil((s_range[i][0] - l) / (w*2+1))
        l = s_range[i][1] + 1
        i += 1
    
    # 마지막 기지국 이후 영역을 처리합니다.
    if s_range[-1][1] < n:
        answer += math.ceil((n - s_range[-1][1]) / (w*2+1))

    return answer
