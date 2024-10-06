# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

result = 0
stack = []
visited = [False] * n
visited_right_down = [False] * (n*2)
visited_left_up = [False] * (n*2)
def dfs():
    global result
    r = len(stack)
    if r == n:
        result += 1
        return
    
    for i in range(n):
        if not visited[i] and not visited_right_down[r-i+n] and not visited_left_up[r+i]:
            visited[i] = True
            visited_right_down[r-i+n] = True
            visited_left_up[r+i] = True
            stack.append(i)
            dfs()
            stack.pop()
            visited[i] = False
            visited_right_down[r-i+n] = False
            visited_left_up[r+i] = False


dfs()
print(result)
