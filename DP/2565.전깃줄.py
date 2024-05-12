# 두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다. 합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.

# 예를 들어, < 그림 1 >과 같이 전깃줄이 연결되어 있는 경우 A의 1번 위치와 B의 8번 위치를 잇는 전깃줄, A의 3번 위치와 B의 9번 위치를 잇는 전깃줄, A의 4번 위치와 B의 1번 위치를 잇는 전깃줄을 없애면 남아있는 모든 전깃줄이 서로 교차하지 않게 된다.


import sys

input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

# A 전봇대 기준으로 정렬
array.sort(key=lambda x: x[0])

d = [1] * n

# 가장 긴 증가하는 부분 수열 구해서
for i in range(n):
    for j in range(i):
        if array[i][1] > array[j][1] and d[i] < d[j]+1:
            d[i] = d[j]+1

# 나머지 전깃줄을 제거
print(n-max(d))