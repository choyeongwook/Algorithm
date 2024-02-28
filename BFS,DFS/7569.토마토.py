# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
from collections import deque
import sys

M, N, H = map(int, sys.stdin.readline().split())


array = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

visited = [[[False] * M for _ in range(N)] for _ in range(H)]


directions = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if array[i][j][k] == 1:
                queue.append((i, j, k))
                visited[i][j][k] = True

while queue:
    x, y, z = queue.popleft()
    
    for dx, dy, dz in directions:
        nx, ny, nz = x+dx, y+dy, z+dz

        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and not visited[nx][ny][nz] and array[nx][ny][nz] == 0:
            queue.append((nx,ny,nz))
            visited[nx][ny][nz] = True
            array[nx][ny][nz] = array[x][y][z] + 1

maximum = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            maximum = max(maximum, array[i][j][k])
            if array[i][j][k] == 0:
                print(-1)
                exit(0)

print(maximum - 1)