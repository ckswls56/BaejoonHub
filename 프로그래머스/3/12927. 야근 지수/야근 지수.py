import heapq as h

def solution(n, works):
    answer = 0

    # Create a max-heap
    works = [-work for work in works]
    h.heapify(works)

    while n > 0:
        if not works:
            break
        max_work = -h.heappop(works)
        if max_work > 0:
            h.heappush(works, -(max_work - 1))
        n -= 1

    for work in works:
        answer += work ** 2

    return answer