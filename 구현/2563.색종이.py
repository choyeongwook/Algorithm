# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.
# 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
# N <= 100

import sys

N = int(input())

array = []

for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

    
paper = [[0 for _ in range(100)] for _ in range(100)]

for x, y in array:
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

print(sum(map(sum, paper)))