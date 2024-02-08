from collections import Counter

def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    res = 0
    for t in topping:
        dic[t] -= 1
        set_dic.add(t)
        if dic[t] == 0:
            dic.pop(t)
        if len(dic) == len(set_dic):
            res += 1
    return res