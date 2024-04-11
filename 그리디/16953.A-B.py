# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다. 
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

from collections import deque

A, B = map(int, input().split())

# 1. A = A*2
# 2. A = A*10 + 1

queue = deque()
queue.append((A, 1))  # 숫자, 카운트
current = A
result = -1
while queue:
    current, count = queue.popleft()

    next_1 = current * 2
    next_2 = current * 10 + 1

    if next_1 == B or next_2 == B:
        result = count+1
        break

    if next_1 < B:
        queue.append((next_1, count+1))
    
    if next_2 < B:
        queue.append((next_2, count+1))
print(result)