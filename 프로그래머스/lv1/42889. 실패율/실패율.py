def solution(N, stages):
    fail = [0 for _ in range(N+2)]
    sucess = [0 for _ in range(N+2)]
    
    for s in stages :
        fail[s] += 1
        for j in range(1, s+1):  # 최적화: 현재 스테이지까지의 정보만 업데이트
            sucess[j] += 1
    
    ratio = []
    for i in range(1, N+1):
        if sucess[i] == 0:
            ratio.append((i, 0))
        else:
            ratio.append((i, fail[i] / sucess[i]))
    
    ratio.sort(key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in ratio]
    return answer
