n = int(input())

array = list(map(int, input().split()))

INF = 9876543221

d = [INF] * n
d[0] = 0

for i in range(n):
    for j in range(1, array[i]+1):
        if i+j < n:
            d[i+j] = min(d[i+j], d[i]+1)

if d[-1] == INF:
    print(-1)
else:
    print(d[-1])