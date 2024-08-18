def solution(sticker):
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    elif n == 2:
        return max(sticker[0], sticker[1])
    
    d_1 = [0] * n
    d_2 = [0] * n
    
    d_1[0] = sticker[0]
    d_1[1] = max(sticker[0], sticker[1])
    for i in range(2, n-1):
        d_1[i] = max(d_1[i-1], d_1[i-2] + sticker[i])
    
    d_2[1] = sticker[1]
    d_2[2] = max(sticker[1], sticker[2])
    for i in range(3, n):
        d_2[i] = max(d_2[i-1], d_2[i-2] + sticker[i])
        
    return max(d_1[n-2], d_2[n-1])