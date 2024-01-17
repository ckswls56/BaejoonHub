def dfs(numbers, current_sum, target):
    if not numbers:
        return 1 if current_sum == target else 0

    ret = 0

    ret += dfs(numbers[1:], current_sum - numbers[0], target)
    ret += dfs(numbers[1:], current_sum + numbers[0], target)

    return ret

def solution(numbers, target):
    answer = dfs(numbers, 0, target)
    return answer
