import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    heappush(heap, int(input()))


result = 0
for _ in range(n-1):
    a = heappop(heap)
    b = heappop(heap)
    result += a+b
    heappush(heap, a+b)

print(result)