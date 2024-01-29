from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    current_weight = 0
    
    while truck_weights or q:
        answer += 1

        if q and answer - q[0][1] == bridge_length:
            current_weight -= q.popleft()[0]

        if truck_weights and current_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            q.append((truck, answer))
            current_weight += truck

    return answer
