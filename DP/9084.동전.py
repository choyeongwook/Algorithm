import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    
    d = [0] * (m+1)
    d[0] = 1
    for coin in coins:
        for i in range(coin, m+1):
            d[i] += d[i-coin]
    
    print(d[m])