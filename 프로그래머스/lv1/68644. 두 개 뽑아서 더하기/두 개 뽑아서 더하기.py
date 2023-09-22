from itertools import combinations

def solution(numbers):
    answer = []
    for n in combinations(numbers, 2):
        s = sum(n)
        if s not in answer:
            answer.append(s)
    answer.sort()
    return answer
