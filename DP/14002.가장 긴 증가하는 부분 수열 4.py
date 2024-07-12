import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

d = [1] * n
results = []
for value in array:
    results.append([value])

max_index = 0
for i in range(1, n):
    for j in range(i):
        if array[i] > array[j] and d[i] < d[j]+1:
            d[i] = d[j]+1
            results[i] = results[j]+[array[i]]
    if d[max_index] < d[i]:
        max_index = i
        
print(d[max_index])
print(*results[max_index])