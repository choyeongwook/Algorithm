# 여행을 떠난 세준이는 지도를 하나 구하였다. 이 지도는 아래 그림과 같이 직사각형 모양이며 여러 칸으로 나뉘어져 있다. 한 칸은 한 지점을 나타내는데 각 칸에는 그 지점의 높이가 쓰여 있으며, 각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능하다.


# 현재 제일 왼쪽 위 칸이 나타내는 지점에 있는 세준이는 제일 오른쪽 아래 칸이 나타내는 지점으로 가려고 한다. 그런데 가능한 힘을 적게 들이고 싶어 항상 높이가 더 낮은 지점으로만 이동하여 목표 지점까지 가고자 한다. 위와 같은 지도에서는 다음과 같은 세 가지 경로가 가능하다.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * m for _ in range(n)]
d[n-1][m-1] = 1

no_path = [[False] * m for _ in range(n)]

def dfs(array, x, y):
    for dx, dy in ((0,1), (1,0), (-1,0), (0,-1)):
        nx, ny = x+dx, y+dy

        if 0 <= nx < n and 0 <= ny < m and array[nx][ny] < array[x][y]:
            if d[nx][ny] == 0 and not no_path[nx][ny]: # 새로 가본 길에서만 dfs
                dfs(array, nx, ny)
            
            # 나오면서 경로의 수 계산
            if d[nx][ny] > 0:
                d[x][y] += d[nx][ny]
            
            # 가봤는데 경로 없음
            if d[x][y] == 0:
                no_path[x][y] = True
dfs(array, 0, 0)

print(d[0][0])
