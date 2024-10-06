import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)] 

for _ in range(m):
    a, b, cost = map(int, input().split())
    
    graph[a].append((b, cost))

start, end = map(int, input().split())

distance = [1e9] * (n+1)

distance[start] = 0

heap = []
heappush(heap, (start, 0))

while heap:
    cur_node, cur_cost = heappop(heap)
    if distance[cur_node] < cur_cost:
        continue
    
    for next_node, next_cost in graph[cur_node]:
        cost_sum = cur_cost + next_cost
        if cost_sum < distance[next_node]:
            distance[next_node] = cost_sum
            heappush(heap, (next_node, cost_sum))

print(distance[end])