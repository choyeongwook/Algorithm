# 준규는 N×M 크기의 미로에 갇혀있다. 미로는 1×1크기의 방으로 나누어져 있고, 각 방에는 사탕이 놓여져 있다. 미로의 가장 왼쪽 윗 방은 (1, 1)이고, 가장 오른쪽 아랫 방은 (N, M)이다.

# 준규는 현재 (1, 1)에 있고, (N, M)으로 이동하려고 한다. 준규가 (r, c)에 있으면, (r+1, c), (r, c+1), (r+1, c+1)로 이동할 수 있고, 각 방을 방문할 때마다 방에 놓여져있는 사탕을 모두 가져갈 수 있다. 또, 미로 밖으로 나갈 수는 없다.

# 준규가 (N, M)으로 이동할 때, 가져올 수 있는 사탕 개수의 최댓값을 구하시오.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = []

for _ in range(n):
    array.append(list(map(int, input().split())))


# 대각선으로 가는 경우는 가로-세로 혹은 세로-가로보다 무조건 작거나 같으므로 무시

# 각 경우마다 max(d[i-1][j], d[위][i][j-1]) + array[i][j] 가 현재 최댓값

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j > 0:
            array[i][j] += array[i][j-1]
        elif j == 0 and i > 0:
            array[i][j] += array[i-1][j]
        else:
            array[i][j] = max(array[i-1][j], array[i][j-1]) + array[i][j]

print(array[-1][-1])