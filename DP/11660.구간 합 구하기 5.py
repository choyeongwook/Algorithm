# N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

# 예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

# 1	2	3	4
# 2	3	4	5
# 3	4	5	6
# 4	5	6	7
# 여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

# 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 0,0 부터 구간 합 저장
d = [[0 for _ in range(n)] for _ in range(n)]

temp_sum = 0
for i in range(n):
    temp_sum += array[0][i]
    d[0][i] = temp_sum

for i in range(1, n):
    temp_sum = 0
    for j in range(n):
        temp_sum += array[i][j]
        d[i][j] = d[i-1][j] + temp_sum

# for i in d:
#     print(i)
# 1,1 부터 구간 합을 저장하고
# 계산이 필요할 때 마다
# d[x2][y2] - d[x2-x1][y2] - d[x2][y2-y1] + 겹치는 부분 d[x2-x1][y2-y1]

for _ in range(m):
    x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split()) # index 접근을 위해 1 뺌
    
    result = d[x2][y2] # - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1]

    if x1 > 0:
        result -= d[x1-1][y2]
    if y1 > 0:
        result -= d[x2][y1-1]
    if x1 > 0 and y1 > 0:
        result += d[x1-1][y1-1]

    print(result)