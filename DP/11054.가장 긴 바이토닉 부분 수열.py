# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

# 예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

# 수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

n = int(input())

array = list(map(int,input().split()))

d = [1] * n
d_reverse = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j] and d[i] < d[j]+1:
            d[i] = d[j]+1  # 가장 긴 증가하는 부분 수열

for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        print(j)
        if array[i] > array[j] and d_reverse[i] < d_reverse[j]+1:
            d_reverse[i] = d_reverse[j]+1 # 반대방향

result = 0
for i in range(n):
    if d[i] + d_reverse[i] > result:
        result = d[i] + d_reverse[i]

print(result - 1)