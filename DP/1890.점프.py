# N×N 게임판에 수가 적혀져 있다. 이 게임의 목표는 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 점프를 해서 가는 것이다.

# 각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리를 의미한다. 반드시 오른쪽이나 아래쪽으로만 이동해야 한다. 0은 더 이상 진행을 막는 종착점이며, 항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야 한다. 한 번 점프를 할 때, 방향을 바꾸면 안 된다. 즉, 한 칸에서 오른쪽으로 점프를 하거나, 아래로 점프를 하는 두 경우만 존재한다.

# 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 이동할 수 있는 경로의 개수를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    array.append(list(map(int,input().split())))

result = 0

path_count = [[0] * n for _ in range(n)] 
path_count[-1][-1] = 1

def dfs(array, x, y):
    global result
    power = array[x][y]

    # 목표 도착 시 종료
    if power == 0:
        result += 1
        return True
    else:
        for dx, dy in ((0,power), (power,0)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if path_count[nx][ny] == 0: # 경로 찾아본 적 없는 곳만 dfs
                    dfs(array, nx, ny)
                path_count[x][y] += path_count[nx][ny]
                # path_count[]

dfs(array,0,0)
# print(result)
print(path_count[0][0])
# for path in path_count:
#     print(path)
