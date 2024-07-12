import sys
input = sys.stdin.readline
from copy import deepcopy

n = int(input())

array = list(map(int, input().split()))
d = [[array[0], array[0]], [array[1], array[1]], [array[2], array[2]]]

for i in range(1, n):
    array = list(map(int, input().split()))
    temp_result = [[0,0], [0,0], [0,0]]
    for j in range(3):
        if j == 0:
            temp_result[0][0] = array[j] + max(d[0][0], d[1][0]) # max
            temp_result[0][1] = array[j] + min(d[0][1], d[1][1]) # min
        elif j == 1:
            temp_result[1][0] = array[j] + max(d[0][0], d[1][0], d[2][0]) # max
            temp_result[1][1] = array[j] + min(d[0][1], d[1][1], d[2][1]) # min
        else:
            temp_result[2][0] = array[j] + max(d[1][0], d[2][0]) # max
            temp_result[2][1] = array[j] + min(d[1][1], d[2][1]) # min
    d = deepcopy(temp_result)


print(max(map(max, d)), min(map(min, d)))