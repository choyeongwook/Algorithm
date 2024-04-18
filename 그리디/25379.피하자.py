# 음이 아닌 정수로 이루어진 길이 N의 배열 A = [A1, A2, · · · , AN]가 있다. 배열 A에서 인접한 두 수를 교환하는 시행을 원하는 만큼 할 수 있다. 이 때, 홀수와 짝수가 인접한 경우가 최대 1번 등장하도록 하는 시행의 최소 횟수를 구하여라. 단, 0 또한 짝수로 간주함에 유의하라.

# 예를 들어, 아래 그림과 같이 A = [4, 5, 1, 0]인 상황을 살펴보자. 이 경우, 마지막 두 원소를 교환하는 시행 과 가운데 두 원소를 교환하는 시행을 차례로 수행하면 A가 [4, 0, 5, 1]이 되어 홀수와 짝수가 인접한 경우가 최대 1번 등장하도록 할 수 있다.

n = int(input())

array = list(map(int, input().split()))


even_count = 0
odd_count = 0

result1 = 0
result2 = 0
for i in range(n):
    if array[i] % 2 == 0:
        result1 += odd_count
        even_count += 1
    else:
        result2 += even_count
        odd_count += 1
        
print(min(result1, result2))