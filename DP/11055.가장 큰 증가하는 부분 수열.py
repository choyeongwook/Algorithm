# 수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가하는 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

n = int(input())

array = list(map(int, input().split()))

d = [0] * (n)

for i in range(n):
    d[i] = array[i]
    for j in range(i-1, -1, -1):
        if array[j] < array[i]:
            d[i] = max(d[i], array[i] + d[j])

print(max(d))