# 총 N개의 문자열로 이루어진 집합 S가 주어진다.

# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

s = []
array = []

for _ in range(n):
    s.append(input().rstrip())

for _ in range(m):
    array.append(input().rstrip())


result = 0

for str in array:
    if str in s:
        result+=1

print(result)