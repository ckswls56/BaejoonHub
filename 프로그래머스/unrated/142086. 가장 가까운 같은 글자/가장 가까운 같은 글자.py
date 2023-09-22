def solution(s):
    # 결과를 저장할 리스트 초기화
    result = []
    # 각 글자의 마지막 등장 위치를 저장할 딕셔너리 초기화
    last_occurrence = {}
    
    # 문자열을 순회하면서 각 글자의 가장 가까운 이전 등장 위치 계산
    for i, char in enumerate(s):
        # 딕셔너리에 글자가 이미 등장한 경우
        if char in last_occurrence:
            # 현재 위치와 이전 등장 위치의 차이를 결과에 저장
            result.append(i - last_occurrence[char])
        else:
            # 글자가 처음 등장한 경우 -1을 결과에 저장
            result.append(-1)
        # 현재 글자의 등장 위치를 업데이트
        last_occurrence[char] = i
    
    return result