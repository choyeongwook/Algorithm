# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

n = int(input())

d = [0] * (n+1) # 최소 횟수를 저장하는 배열
before_index_list = [0] * (n+1) # 자기의 이전 인덱스만 저장
# 이전에 계산한 최소 횟수를 사용하여 계산 가능

for i in range(2, n+1):
    d[i] = d[i-1] + 1 # 기본적으로 이전 값 + 1
    before_index = i-1
    
    if i % 2 == 0 and d[i//2]+1 < d[i]: # 2로 나누어 떨어지면 -> 2로 나눈 값에서 *2연산을 한 번만 하면 됨
        d[i] = d[i//2] + 1
        before_index = i//2
    if i % 3 == 0 and d[i//3]+1 < d[i]: # 3로 나누어 떨어지면 -> 3로 나눈 값에서 *3연산을 한 번만 하면 됨
        d[i] = d[i//3] + 1
        before_index = i//3

    before_index_list[i] = before_index


def print_before_recursive(num):
    print(num, end=' ')
    if before_index_list[num] != 0:
        print_before_recursive(before_index_list[num])



print(d[n])
print_before_recursive(n)