def solution(n, stations, w):
    
    array = []
    left, right = 0, 0
    for s in stations:
        s_left, s_right = s-w, s+w
        if s_left == 0:
            left, right = s_left, s_right
            continue
        
        if s_left > right+1: # 안 겹침
            array.append(s_left-right-1) # 안 겹치는 부분 array에 추가
            left, right = s_left, s_right # 새로 시작
        else: # 겹침
            right = s_right
    if right < n:
        array.append(n-right)
    # print(array)
    result = 0
    for r in array: # range(1,3)
        result += r // (w*2+1) + 1
        if r % (w*2+1) == 0:
            result -= 1
    return result