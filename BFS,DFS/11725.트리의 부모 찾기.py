# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

import sys
from collections import deque

N = int(sys.stdin.readline())

array = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = [0] * (N-1)

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    array[a].append(b)
    array[b].append(a)


queue = deque()
parent = 1
queue.append((array[1], parent))
visited[1] = True

while queue:
    child_list, parent = queue.popleft()

    for child in child_list:
        if not visited[child]:
            queue.append((array[child], child))
            visited[child] = True
            result[child-2] = parent

for r in result:
    print(r)