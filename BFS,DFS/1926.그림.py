import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
directions = ((1,0),(-1,0),(0,1),(0,-1))
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

def bfs(start_x, start_y):
    queue = deque()
    area = 1
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                area += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return area

max_area = 0
count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and array[i][j] == 1:
            max_area = max(max_area, bfs(i, j))
            count += 1

print(count)
print(max_area)
