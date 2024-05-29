# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.



n = int(input())

result = 0
stack = []

y_direct = [False] * n
x_minus_y = [False] * (n*2)
x_minus_n_minus_y = [False] * (n*2)

def dfs():
    global result
    x = len(stack)
    # n개를 꽉 채웠으면 리턴
    if x == n:
        result += 1
        return

    for y in range(n):
        if y_direct[y] or x_minus_y[x-y+n] or x_minus_n_minus_y[x-(n-y)+n]:
            continue

        stack.append(y)
        y_direct[y] = True
        x_minus_y[x-y+n] = True
        x_minus_n_minus_y[x-(n-y)+n] = True

        dfs()

        stack.pop()
        y_direct[y] = False
        x_minus_y[x-y+n] = False
        x_minus_n_minus_y[x-(n-y)+n] = False

dfs()

print(result)