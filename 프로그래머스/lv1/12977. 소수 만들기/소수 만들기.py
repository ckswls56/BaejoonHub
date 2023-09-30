import itertools
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def solution(nums):
    answer = 0
    for c in itertools.combinations(nums, 3):
        if is_prime(sum(c)) and sum(c) <= 3000:
            answer += 1
    return answer
