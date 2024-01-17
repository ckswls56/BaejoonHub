def dfs(computers, n, visit):
    if visit[n]:
        return 0

    visit[n] = True
    ret = 1

    for i, c in enumerate(computers[n]):
        if c and not visit[i]:
            ret += dfs(computers, i, visit)

    return ret

def solution(n, computers):
    answer = 0
    visit = [False] * n

    for i in range(n):
        answer += min(1, dfs(computers, i, visit))

    return answer
