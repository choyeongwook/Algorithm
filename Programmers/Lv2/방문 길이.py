def solution(dirs):
    direction_dic = {'U': (1,0), 'L': (0,-1), 'D': (-1,0), 'R': (0,1)}
    reverse = {'U': 'D', 'L': 'R', 'D': 'U', 'R': 'L'}
    visited = {}
    count = 0
    
    x, y = 0, 0
    for dir in dirs:
        dx, dy = direction_dic[dir]
        nx, ny = x+dx, y+dy
        
        # 맵 탈출 시 continue
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        
        if visited.get((x, y, dir)) is None:
            count += 1
            visited[(x, y, dir)] = True
            visited[(nx, ny, reverse[dir])] = True # 반대도 저장
        
        x, y = nx, ny
    return count