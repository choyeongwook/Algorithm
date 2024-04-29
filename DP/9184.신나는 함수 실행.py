# 재귀 호출만 생각하면 신이 난다! 아닌가요?

# 다음과 같은 재귀함수 w(a, b, c)가 있다.

# if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
#     1

# if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
#     w(20, 20, 20)

# if a < b and b < c, then w(a, b, c) returns:
#     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

# otherwise it returns:
#     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
# 위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)

# a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

d = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]


for a in range(1, 21):
    for b in range(1, 21):
        for c in range(1, 21):
            # if a < b and b < c, then w(a, b, c) returns:
            # w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            if a < b and b < c:
                d[a][b][c] = d[a][b][c-1] + d[a][b-1][c-1] - d[a][b-1][c]
            else:
                # otherwise it returns:
                # w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
                d[a][b][c] = d[a-1][b][c] + d[a-1][b-1][c] + d[a-1][b][c-1] - d[a-1][b-1][c-1]

while True:
    a, b, c = map(int, input().split())
    result = 0
    if a == -1 and b == -1 and c == -1:
        break
    if a < 1 or b < 1 or c < 1:
        result = 1
    elif a > 20 or b > 20 or c > 20:
        result = d[20][20][20]
    else:
        result = d[a][b][c]
    print(f'w({a}, {b}, {c}) = {result}')