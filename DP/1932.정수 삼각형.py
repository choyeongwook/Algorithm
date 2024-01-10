# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
#이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
#아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
# 삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

import sys

N = int(input())

array = []

for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

    
d = [[0] * (i+1) for i in range(N)]

d[0][0] = array[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0: # 왼쪽 끝
            d[i][j] = d[i-1][j] + array[i][j]
        elif j == i: # 오른쪽 끝
            d[i][j] = d[i-1][j-1] + array[i][j]
        else: # 가운데
            d[i][j] = max(d[i-1][j], d[i-1][j-1]) + array[i][j]

print(max(d[N-1]))