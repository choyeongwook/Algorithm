# 유현이가 새 집으로 이사했다. 새 집의 크기는 N×N의 격자판으로 나타낼 수 있고, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타낼 수 있다. 여기서 r은 행의 번호, c는 열의 번호이고, 행과 열의 번호는 1부터 시작한다. 각각의 칸은 빈 칸이거나 벽이다.

# 오늘은 집 수리를 위해서 파이프 하나를 옮기려고 한다. 파이프는 아래와 같은 형태이고, 2개의 연속된 칸을 차지하는 크기이다.



# 파이프는 회전시킬 수 있으며, 아래와 같이 3가지 방향이 가능하다.



# 파이프는 매우 무겁기 때문에, 유현이는 파이프를 밀어서 이동시키려고 한다. 벽에는 새로운 벽지를 발랐기 때문에, 파이프가 벽을 긁으면 안 된다. 즉, 파이프는 항상 빈 칸만 차지해야 한다.

# 파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 파이프는 밀면서 회전시킬 수 있다. 회전은 45도만 회전시킬 수 있으며, 미는 방향은 오른쪽, 아래, 또는 오른쪽 아래 대각선 방향이어야 한다.

# 파이프가 가로로 놓여진 경우에 가능한 이동 방법은 총 2가지, 세로로 놓여진 경우에는 2가지, 대각선 방향으로 놓여진 경우에는 3가지가 있다.

# 아래 그림은 파이프가 놓여진 방향에 따라서 이동할 수 있는 방법을 모두 나타낸 것이고, 꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있다.

# dfs
# x좌표, y좌표, 현재방향 저장
# dp배열에 경로의 수 저장

import sys

input = sys.stdin.readline

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

# 방향: 0(오른쪽),1(대각선),2(아래)
available_directions = ((0, 1), (0, 1, 2), (1, 2))

next = ((0, 1), (1, 1), (1, 0))


#      도착한 방향                  y좌표              x좌표
d = [[[-1 for _ in range(3)] for _ in range(n)] for _ in range(n)]

# 시작 포인트: 한 칸 오른쪽, 도착방향은 ->
# d[0][1][0] = 1


def dfs(array, x, y, direction):
    # 도착점 도달 시 경우의 수 1 리턴
    if x == n-1 and y == n-1:
        return 1
    
    # 가본 곳 일 시 저장한 경우의 수 리턴
    if d[x][y][direction] != -1:
        return d[x][y][direction]
    
    # 가 본 곳 체크
    d[x][y][direction] = 0

    for next_direction in available_directions[direction]:
        # next_direction: 도착한 방향에 맞는 가능한 다음 방향
        dx, dy = next[next_direction]
        nx, ny = x+dx, y+dy
                                 # 벽이 아닐 경우
        if nx < n and ny < n and array[nx][ny] != 1:
            # 대각선 벽 처리
            if next_direction == 1 and (array[nx][y] == 1 or array[x][ny] == 1):
                continue
        
            d[x][y][direction] += dfs(array, nx, ny, next_direction)
    
    return d[x][y][direction]
        

result = dfs(array, 0, 1, 0)

print(result)