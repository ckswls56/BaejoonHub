def solution(strings, n):
    # 문자열을 정렬하는 사용자 정의 함수
    def custom_sort(s):
        return (s[n], s)
    
    # sorted() 함수를 사용하여 정렬
    sorted_strings = sorted(strings, key=custom_sort)
    
    return sorted_strings
