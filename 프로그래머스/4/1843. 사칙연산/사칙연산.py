def solution(arr):
    ## +연산은 상관없지만 -연산은 두가지 경우의 수로 나뉜다.
    ## 전체에 대해서 - 연산, 나머지 더한값과 마지막 - 연산
    ## 최대값을 구하기 위해서 min,max를 계속 추적해야 한다.
    mins,maxs = 0,0
    summation = 0
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == '+':
            continue
        elif arr[i] == '-':
            tmp_mins,tmp_maxs = mins,maxs
            mins = min(-(summation+tmp_maxs),tmp_mins-summation)
            minus_v = int(arr[i+1])
            maxs = max(-(summation+tmp_mins),(summation-minus_v)-minus_v+tmp_maxs)
            summation = 0
        else :
            summation += int(arr[i])
    maxs += summation
    return maxs
    
    