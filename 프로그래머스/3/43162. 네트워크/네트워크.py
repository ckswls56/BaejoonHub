def dfs(computers, n, visit):
    if visit[n]:
        return 0

    visit[n] = True
    

    for i, c in enumerate(computers[n]):
        if c and not visit[i]:
            dfs(computers, i, visit)

    return 1

def solution(n, computers):
    answer = 0
    visit = [False] * n

    for i in range(n):
        answer += dfs(computers, i, visit)

    return answer
