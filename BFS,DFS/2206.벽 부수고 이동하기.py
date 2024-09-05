import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

array = []
directions = ((0,1), (0,-1), (1,0), (-1,0))

for _ in range(n):
    array.append(list(map(int, list(input().rstrip()))))


visited = [[False] * m for _ in range(n)]
visited_is_used = [[False] * m for _ in range(n)]

queue = deque()
queue.append((0, 0, False, 1))

# 내가 벽 깬거 썼을 경우: visited_is_used만 확인 가능, visited_is_used일 경우 실행 불가
# 내가 벽 깬거 안 썼을 경우 : visited 확인
# 벽일 경우: 현재 벽 안깼으면 깨고 진행, 현재 벽 깼으면 못 진행
while queue:
    x, y, is_used, count = queue.popleft()
    
    if x == n-1 and y == m-1:
            print(count)
            exit(0)
    
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        
        if 0 <= nx < n and 0 <= ny < m:
            # 다음 지역이 길이고, 벽부수기를 사용하지 않았을 경우
            if array[nx][ny] == 0 and is_used == False:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, False, count+1))
            # 다음 지역이 길이고, 벽부수기를 사용했을 경우
            elif array[nx][ny] == 0 and is_used == True:
                if not visited_is_used[nx][ny]:
                    visited_is_used[nx][ny] = True
                    queue.append((nx, ny, True, count+1))
            # 다음 지역이 벽이고, 벽부수기를 사용하지 않았을 경우
            elif array[nx][ny] == 1 and is_used == False:
                if not visited_is_used[nx][ny]:
                    visited_is_used[nx][ny] = True
                    queue.append((nx, ny, True, count+1))
            # 다음 지역이 벽이고, 벽부수기를 사용했을 경우
            else:
                continue
            
print(-1)