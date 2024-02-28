# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

import sys
from collections import deque

# 8각
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]

def bfs(array, start, visited, w, h):
    x, y = start
    visited[x][y] = True

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and array[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
    

while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    array = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if array[i][j] == 1 and not visited[i][j]:
                bfs(array, (i,j), visited, w, h)
                count += 1
    print(count)


    