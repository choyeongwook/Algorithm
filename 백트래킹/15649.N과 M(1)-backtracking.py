# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

n, m = map(int, input().split())
 


stack = []
visited = [False] * (n+1)

def dfs():
    if len(stack) == m:
        print(*stack)
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            dfs()
            stack.pop()
            visited[i] = False

dfs()