# 수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.

n = int(input())

array = list(map(int, input().split()))

d = [1] * (n)

for i in range(n):
    for j in range(i-1, -1, -1):
        if array[i] < array[j]:
            d[i] = max(d[i], d[j] + 1) 


print(max(d))
