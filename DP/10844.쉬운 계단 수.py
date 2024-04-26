# 45656이란 수를 보자.

# 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.


n = int(input())

d = [[0]*10 for _ in range(n+1)] 
# 2차원 배열
# 마지막 자릿수 개수 저장 (0~9)

d[1] = [0,1,1,1,1,1,1,1,1,1] # 마지막 자리수의 개수


for i in range(1, n):
    for j in range(10):
        if j-1 >= 0:
            d[i+1][j-1] += d[i][j]
        if j+1 <= 9:
            d[i+1][j+1] += d[i][j]


print(sum(d[n])%1000000000)