def solution(myString, pat):
    idx = myString.rfind(pat)
    answer = myString [:idx+len(pat)]
    return answer