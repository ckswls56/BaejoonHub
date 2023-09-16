from itertools import combinations

def solution(a, b, c, d):
    numbers=[a,b,c,d]
    num_count = {a: 0, b: 0, c: 0, d: 0}
    
    for n in numbers:
        num_count[n] += 1
    
    max_count = max(num_count.values())
    
    if max_count == 4:
        answer = 1111 * a
    elif max_count == 3:
        for num, count in num_count.items():
            if count == 1:
                q = num
                break
        p = [num for num in numbers if num != q][0]
        answer = (10 * p + q) ** 2
    elif max_count == 2 :
        for i in num_count.values() :
            if i != 2 :
                for combo in combinations(numbers, 2):
                    if combo[0] != combo[1] and num_count[combo[0]] != 2 and num_count[combo[1]] != 2:
                        return combo[0] * combo[1]
        if a==b :
            answer = (a+c) * abs(a-c)
        else :
            answer = (a+b) * abs(a-b)
        
                
    else:
        answer = min(numbers)
        
    return answer
        
    return answer
