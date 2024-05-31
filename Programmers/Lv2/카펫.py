def solution(brown, yellow):
    # 제곱수까지 진행
    for y in range(1, int((brown+yellow)**0.5+1)):
        if (brown+yellow) % y != 0:
            continue
        print(y)
        x = (brown+yellow) // y
        
        if yellow == (x-2)*(y-2):
            return [x,y]
    return -1