def largestNumber(numbers):
    # 정수를 문자열로 변환하여 비교 함수를 사용하여 정렬
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x * 10, reverse=True)  # 문자열을 10번 반복하여 비교
    
    # 모든 숫자가 0일 경우에는 "0"을 반환
    if numbers[0] == "0":
        return "0"
    
    # 숫자들을 이어 붙여 문자열로 변환하여 반환
    return ''.join(numbers)


def solution(numbers):
    return largestNumber(numbers)