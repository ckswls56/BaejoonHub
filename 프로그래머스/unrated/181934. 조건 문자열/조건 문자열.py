def solution(ineq, eq, n, m):
    if ineq == '>' and eq == '=' :
        if n >= m :
            answer = 1
        else :
            answer = 0
    if ineq == '>' and eq == '!' :
        if n > m :
            answer = 1
        else :
            answer = 0
    if ineq == '<' and eq == '=' :
        if n <= m :
            answer = 1
        else :
            answer = 0
    if ineq == '<' and eq == '!' :
        if n < m :
            answer = 1
        else :
            answer = 0
    return answer