from collections import Counter

def solution(gems):
    if len(set(gems)) == 1:
        return (1, 1)

    gem_count = len(set(gems))
    gem_counter = Counter()
    left, right = 0, 0
    min_length = float('inf')
    answer = [0, len(gems) - 1]

    while right < len(gems):
        gem_counter[gems[right]] += 1
        right += 1

        while len(gem_counter) == gem_count:
            if right - left < min_length:
                min_length = right - left
                answer = [left + 1, right]

            gem_counter[gems[left]] -= 1
            if gem_counter[gems[left]] == 0:
                del gem_counter[gems[left]]
            left += 1

    return answer