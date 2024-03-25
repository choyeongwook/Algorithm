# 눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

# 예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.

# <그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.

# M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

import sys
sys.setrecursionlimit(100000)

M, N, K = map(int, input().split())

array = [[0] * M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            array[i][j] = 1

directions = [(0,1), (0,-1), (1,0), (-1,0)]

def dfs(start):
    global count
    x, y = start
    array[x][y] = 1
    count += 1

    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < M and array[nx][ny] != 1:
            dfs((nx,ny))


count_array = []
for i in range(N):
    for j in range(M):
        if array[i][j] == 0:
            count = 0
            dfs((i,j))
            count_array.append(count)

print(len(count_array))
for value in sorted(count_array):
    print(value, end=' ')