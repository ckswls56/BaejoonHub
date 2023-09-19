def solution(sizes):
    max_w,max_h = 0,0
    for s in sizes :
        w,h = s
        max_w = max(max_w,w,h)
        max_h = max(max_h,min(w,h))
    answer = max_w*max_h
    return answer