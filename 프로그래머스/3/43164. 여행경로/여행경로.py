def dfs(tickets, path):
    if not tickets:
        return path
    
    ret = ['ZZZ']*10000
    
    for i in range(len(tickets)):
        if path[-1] == tickets[i][0]:
            temp = path + [tickets[i][1]]
            ## 알파벳 순으로 앞서는 문자열을 우선으로
            ret = min(ret, dfs(tickets[:i] + tickets[i + 1:], temp))
    
    return ret

def solution(tickets):
    answer = dfs(tickets, ['ICN'])
    return answer
