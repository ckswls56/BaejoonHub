def solution(arr):
    answer = []
    
    for num in arr:
        # answer가 비어있거나, 현재 숫자가 answer의 마지막 숫자와 다른 경우에만 추가
        if not answer or answer[-1] != num:
            answer.append(num)
    
    return answer