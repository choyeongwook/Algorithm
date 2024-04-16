# 위상정렬

# 올해 Z대학 컴퓨터공학부에 새로 입학한 민욱이는 학부에 개설된 모든 전공과목을 듣고 졸업하려는 원대한 목표를 세웠다. 어떤 과목들은 선수과목이 있어 해당되는 모든 과목을 먼저 이수해야만 해당 과목을 이수할 수 있게 되어 있다. 공학인증을 포기할 수 없는 불쌍한 민욱이는 선수과목 조건을 반드시 지켜야만 한다. 민욱이는 선수과목 조건을 지킬 경우 각각의 전공과목을 언제 이수할 수 있는지 궁금해졌다. 계산을 편리하게 하기 위해 아래와 같이 조건을 간소화하여 계산하기로 하였다.

# 한 학기에 들을 수 있는 과목 수에는 제한이 없다.
# 모든 과목은 매 학기 항상 개설된다.
# 모든 과목에 대해 각 과목을 이수하려면 최소 몇 학기가 걸리는지 계산하는 프로그램을 작성하여라.


import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

indegree = [0] * (n+1)

outbound = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    outbound[a].append(b)
    indegree[b] += 1

result = [0] * n

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append((i, 1)) # index, turn

while queue:
    i, turn = queue.popleft()
    result[i-1] = turn
    for j in outbound[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append((j, turn+1))

print(*result)