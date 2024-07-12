from collections import deque

directions = [(0,1),(0,-1),(1,0),(-1,0)]

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    if maps[n-1][m-1] <= 1:
        return -1
    else:
        return maps[n-1][m-1]

    