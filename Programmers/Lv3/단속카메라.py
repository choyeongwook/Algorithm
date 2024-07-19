def solution(routes):
    routes.sort(key=lambda x: (x[0], -x[1]))
    print(routes)
    
    minimum = -30001
    
    result = 0
    
    process = False
    for i, (car_in, car_out) in enumerate(routes):
        if i == 0: # 첫 번째
            minimum = car_out
            result += 1 # +1
            continue

        if car_in <= minimum: # 겹친다면
            minimum = min(minimum, car_out)
        else: # 안겹친다면
            minimum = car_out
            result += 1 # +1
    
    
    return result