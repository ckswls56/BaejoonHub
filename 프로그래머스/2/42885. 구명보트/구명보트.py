from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()

    left, right = 0, len(people) - 1

    while left <= right:
        # Check if the heaviest person can be paired with the lightest person within the weight limit
        if people[left] + people[right] <= limit:
            left += 1  # Move the left pointer to the next person
        right -= 1  # Move the right pointer to the next person
        answer += 1  # Increment the number of boats used

    return answer
