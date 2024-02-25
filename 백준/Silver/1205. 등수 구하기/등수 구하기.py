n, new_point, p = map(int, input().split())
if n:
    score = list(map(int,input().split()))
    score.append(new_point)
    score.sort(reverse=True)
    idx = score.index(new_point) + 1

    if idx > p :
        print(-1)
    else :
        if n==p and new_point == score[-1]:
            print(-1)
        else:
            print(idx)
else :
    print(1)
