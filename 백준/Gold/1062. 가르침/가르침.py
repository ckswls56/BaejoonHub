from itertools import combinations
import sys

input = sys.stdin.readline
n, k = map(int, input().strip().split())

def solve(n, k):
    required = {'a', 'n', 't', 'i', 'c'}
    uniqueList = []
    uniqueSet = set()
    cnt = 0

    for _ in range(n):
        cur = input().strip()
        curSet = set(cur)

        # 무조건 읽을 수 있는 경우 처리
        if curSet == required:
            cnt += 1
            continue

        # 현재 단어에서 'antic'을 제외한 고유 문자를 추가
        curUnique = curSet - required
        if curUnique:
            uniqueList.append(curUnique)
            uniqueSet.update(curUnique)

    # k가 5보다 작으면 무조건 읽을 수 없음
    if k < 5:
        return 0

    # 추가 배울 문자가 없는 경우
    if len(uniqueSet) <= k - 5:
        return cnt + len(uniqueList)

    maxCnt = 0

    # 추가 문자 조합으로 최대 읽을 수 있는 단어 수 계산
    for c in combinations(uniqueSet, k - 5):
        caseSet = set(c)
        tmpAns = sum(1 for uniqueWord in uniqueList if caseSet.issuperset(uniqueWord))
        maxCnt = max(maxCnt, tmpAns)

    return cnt + maxCnt

print(solve(n, k))