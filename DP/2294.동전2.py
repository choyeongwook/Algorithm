# n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

import sys

input = sys.stdin.readline
INF = 987654321

n, k = map(int, input().split())

array = []

for _ in range(n):
    array.append(int(input()))

d = [INF] * (k+1)
d[0] = 0

# 이전 값의 최소 개수로 현재 값 계산

# 1원으로 만들 수 있는 최소 개수
# 5원을 추가해 만들 수 있는 최소 개수
# 12원을 추가해 만들 수 있는 최소 개수
        
# 점화식 : min(   d[i-coin1]+1, d[i-coin2]+1, d[i-coin3]+1   )

for i in range(1, k+1):
    for coin_value in array:
        if i-coin_value < 0: # index out of range
            continue
        if d[i] > d[i-coin_value]+1:
            d[i] = d[i-coin_value]+1

if d[k] == INF:
    print(-1)
else:
    print(d[k])
