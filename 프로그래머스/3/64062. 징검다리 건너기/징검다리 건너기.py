import heapq
from math import inf

def solution(stones, k):
    n = len(stones)

    # 최대 힙 방식으로 각 구간의 최댓값을 구할 것이다.
    queue = []
    answer = inf

    # 먼저 0부터 k - 2 까지 최대 힙에 인덱스와 함께 넣자.
    for i in range(k - 1):
        heapq.heappush(queue, [-stones[i], i])

    # k - 1부턴 하나씩 최대 힙에 넣자.
    # 최대 힙의 맨 앞의 인덱스가 i - k + 1보다 작다면 구간을 벗어난 원소
    # 구간을 벗어난 원소를 전부 pop
    for i in range(k - 1, n):
        heapq.heappush(queue, [-stones[i], i])
        while queue[0][1] < i - k + 1:
            heapq.heappop(queue)
        answer = min(answer, -queue[0][0]) # 답은 각 구간의 최댓값들의 최솟값

    return answer