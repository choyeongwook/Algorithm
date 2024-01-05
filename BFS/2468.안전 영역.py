import sys
from collections import deque

N = int(input())

array = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

direction = [(0,1), (0,-1), (1,0), (-1,0)]

max_height = max(map(max, array))

result = 1

for rain_height in range(1, max_height):
    count = 0

    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and array[i][j] > rain_height:
                count += 1
                # bfs
                queue = deque()
                queue.append((i,j))
                visited[i][j] = True

                while queue:
                    x, y = queue.popleft()
                    
                    for dx, dy in direction:
                        nx, ny = x+dx, y+dy

                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and array[nx][ny] > rain_height:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                    
    result = max(result, count)

print(result)