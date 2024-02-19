from itertools import combinations

def solution(orders, course):
    answer = []
    m = {}
    for order in orders:
        for c in course:
            if len(order) >= c:
                for combo in combinations(order, c):
                    con = frozenset(combo)
                    m[con] = m.get(con, 0) + 1
    
    max_m = {}
    for k, v in m.items():
        if v >= 2:
            max_m[len(k)] = max(max_m.get(len(k),0),v)
            
    for k, v in m.items():
        if v == max_m.get(len(k),0):
            answer.append(''.join(sorted(k)))
    
    answer.sort()
    return answer
