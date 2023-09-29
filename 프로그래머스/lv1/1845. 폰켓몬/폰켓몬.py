
def solution(nums):
    answer = 0
    map = dict()
    for n in nums :
        map[n] = True
    
    if len(map.keys()) <= len(nums)//2:
        return len(map.keys())
    else :
        return len(nums)//2
        