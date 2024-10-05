import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int, input().split()))

d = [0] * (n+1)
d[1] = array[0]
for i in range(2, n+1):
    d[i] = d[i-1] + array[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    
    result = d[j] - d[i-1]
    print(result)
