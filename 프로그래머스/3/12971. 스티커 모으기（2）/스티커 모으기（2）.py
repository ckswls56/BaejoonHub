def solution(sticker):
    if len(sticker) == 1 :
        return sticker[0]
    elif len(sticker) == 2:
        return max(sticker[0],sticker[1])
    elif len(sticker) == 3:
        return max(sticker[0]+sticker[2],sticker[1])

    dp1 = [0 for _ in range(len(sticker)+1)]
    dp1[0] = sticker[0]
    dp1[1] = sticker[1]
    dp1[2] = max(sticker[0]+sticker[2],sticker[1])
    for i in range(3,len(sticker)-1):
        dp1[i] = max(dp1[i-3],dp1[i-2]) + sticker[i]
        
    dp2 = [0 for _ in range(len(sticker)+1)]
    dp2[1] = sticker[1]
    dp2[2] = sticker[2]
    dp2[3] = max(sticker[1]+sticker[3],sticker[2])
    for i in range(4,len(sticker)):
        dp2[i] = max(dp2[i-3],dp2[i-2]) + sticker[i]
 
    return max(max(dp1),max(dp2))