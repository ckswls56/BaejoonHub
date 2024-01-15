from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque()

    # Initialize the queue with tuples
    for i in range(len(progresses)):
        q.append((progresses[i], speeds[i]))

    while q:
        # Update progress values in the queue
        q = deque([(p + s, s) for p, s in q])

        # Count deployable tasks
        cnt = 0
        while q and q[0][0] >= 100:
            q.popleft()
            cnt += 1

        # Append the count to the answer list
        if cnt > 0:
            answer.append(cnt)

    return answer
