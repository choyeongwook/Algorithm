import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

maps = [list(map(int, list(input().rstrip()))) for _ in range(n)]

queue = deque()
queue.append((0,0,0,1))

visited = [[[False]*m for _ in range(n)] for _ in range(k+1)]

directions = ((0,1),(1,0),(0,-1),(-1,0))


while queue:
    x, y, wall, distance = queue.popleft()
    
    if x == n-1 and y == m-1:
        print(distance)
        exit(0)
    
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        
        # 맵 탈출 시 continue
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        # 다음 턴이 길이면
        if maps[nx][ny] == 0 and not visited[wall][nx][ny]:
            # 거리만 +1
            queue.append((nx,ny,wall,distance+1))
            visited[wall][nx][ny] = True
        # 벽이면
        elif maps[nx][ny] == 1 and wall+1 <= k and not visited[wall+1][nx][ny] :
            queue.append((nx,ny,wall+1,distance+1))
            visited[wall+1][nx][ny] = True
    # print(queue)

print(-1)