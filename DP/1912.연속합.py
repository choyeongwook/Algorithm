# n개의 정수로 이루어진 임의의 수열이 주어진다.
# 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
# 단, 수는 한 개 이상 선택해야 한다.
# 예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

N = int(input())
array = list(map(int, input().split()))

d = [0] * N

d[0] = array[0]
current_sum = array[0]

for i in range(1, N):
    if current_sum > 0: # 이전까지 더했던 수가 양수면 연속되게 더해줌
        current_sum += array[i] 
    else:
        current_sum = array[i] # 음수면 새로 시작

    d[i] = max(d[i-1], current_sum)

print(d[N-1])