import heapq

def solution(n, k, enemy):
    max_heap = []
    answer = 0

    for e in enemy:
        heapq.heappush(max_heap, -e)  # 최대 힙으로 사용하기 위해 음수로 저장
        n -= e  # 병사 수 감소

        if n < 0:  # 병사가 부족한 경우
            if k > 0:  # 무적권이 남아있으면
                n += -heapq.heappop(max_heap)  # 가장 많은 적이 등장했던 라운드를 무적권으로 막기
                k -= 1
            else:  # 무적권이 남아있지 않으면 더 이상 라운드를 진행할 수 없음
                break
        
        answer += 1

    return answer
