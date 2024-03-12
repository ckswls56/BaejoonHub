def isDivided(array, n):
    for a in array:
        if a % n != 0:
            return False
    return True

def isNotDivided(array, n):
    for a in array:
        if a % n == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_common_divisors(array):
    if len(array) == 0:
        return []

    # 배열의 첫 번째 요소를 기준으로 최대공약수 초기화
    gcd_value = array[0]
    for num in array[1:]:
        gcd_value = gcd(gcd_value, num)

    # 최대공약수의 약수 찾기
    common_divisors = []
    for i in range(1, int(gcd_value ** 0.5) + 1):
        if gcd_value % i == 0:
            common_divisors.append(i)
            if i != gcd_value // i:  # 제곱수가 아닌 경우에만 추가
                common_divisors.append(gcd_value // i)

    common_divisors.sort()  # 정렬 (선택적)

    return common_divisors

def binarySearch(arrayA, arrayB):
    left = 1
    right = 1000000000
    ret = 0
    for a in find_common_divisors(arrayA):
        if isNotDivided(arrayB,a):
            ret = max(ret,a)
    
    for a in find_common_divisors(arrayB):
        if isNotDivided(arrayA,a):
            ret = max(ret,a)
    
    
    return ret

def solution(arrayA, arrayB):
    answer = binarySearch(arrayA, arrayB)
    return answer