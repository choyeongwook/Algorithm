n = int(input())

d = [0] * (n+1)
if n % 2 == 1:
    print(0)
    exit(0)

d[0] = 1
d[2] = 3

for i in range(4, n+1, 2):
    d[i] += d[i-2] * 3
    for j in range(i-4, -1, -2):
        d[i] += d[j] * 2

print(d[n])