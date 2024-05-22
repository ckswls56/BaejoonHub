answer = []
def hanoi(n,s,m,e):
    if n == 1:
        answer.append((s,e))
    else :
        hanoi(n-1,s,e,m)
        answer.append((s,e))
        hanoi(n-1,m,s,e)

def solution(n):
    hanoi(n,1,2,3)
    return answer