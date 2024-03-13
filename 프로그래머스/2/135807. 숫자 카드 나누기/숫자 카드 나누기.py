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
    common_divisors = set()
    for i in range(1,gcd_value):
        if gcd_value % i == 0:
            common_divisors.add(i)
            common_divisors.add(gcd_value // i)

    return sorted(common_divisors,reverse=True)  # 정렬하여 반환

def search(arrayA, arrayB):
    ret = 0
    for a in find_common_divisors(arrayA):
        if isNotDivided(arrayB,a):
            ret = a
            break
    
    for a in find_common_divisors(arrayB):
        if isNotDivided(arrayA,a):
            ret = max(ret,a)
            break
    
    
    return ret

def solution(arrayA, arrayB):
    answer = search(arrayA, arrayB)
    return answer