# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

# N개의 자연수 중에서 M개를 고른 수열

n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))

stack = []
visited = [False] * n

def dfs():
    if len(stack) == m:
        for index in stack:
            print(array[index], end=' ')
        print()
        return
    
    for i in range(n):
        if visited[i]:
            continue

        stack.append(i)
        visited[i] = True

        dfs()

        stack.pop()
        visited[i] = False

dfs()