import sys
import math

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

b, c = map(int, input().split())

result = 0

for num in array:
    num -= b
    result += 1
    if num > 0:
        result += math.ceil(num / c)
    
print(result)