# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

from collections import deque
import sys

directions = [(2,1), (1,2), (2,-1), (1,-2), (-2,1), (-1,2), (-2,-1), (-1,-2)]

n = int(sys.stdin.readline())

for _ in range(n):
    l = int(sys.stdin.readline())
    array = [[0] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]

    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())

    queue = deque()

    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            break

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny] and array[nx][ny] <= array[x][y]:
                array[nx][ny] = array[x][y] + 1
                queue.append((nx,ny))
                visited[nx][ny] = True
    print(array[end_x][end_y])