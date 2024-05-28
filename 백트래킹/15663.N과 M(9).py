# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# N개의 자연수 중에서 M개를 고른 수열

n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))

stack = []
result = []
visited = [False] * n

def dfs():
    if len(stack) == m:
        print(*stack)
        return
    
    before = 0
    for i in range(n):
        if visited[i] or before == array[i]:
            continue
        
        stack.append(array[i])
        visited[i] = True

        dfs()

        stack.pop()
        before = array[i]
        visited[i] = False

dfs()
