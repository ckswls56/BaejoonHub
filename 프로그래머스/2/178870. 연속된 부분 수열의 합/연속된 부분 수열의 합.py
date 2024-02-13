def solution(sequence, k):
    answer = []
    arr = {0: -1}  # 딕셔너리를 사용하여 인덱스를 저장합니다.
    prefix_sum = 0
    min_range = len(sequence)

    for i, s in enumerate(sequence):
        prefix_sum += s
        if prefix_sum - k in arr:
            start_index = arr[prefix_sum - k] + 1
            end_index = i
            answer.append((start_index, end_index))
            min_range = min(min_range, end_index - start_index)
            if min_range == 0:
                return (start_index, end_index)
        arr[prefix_sum] = i  # 현재 합의 인덱스를 저장합니다.

    return min(answer, key=lambda x: (x[1] - x[0], x[0]))
