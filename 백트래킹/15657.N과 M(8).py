n, m = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

stack = []
def dfs(current):
    if len(stack) == m:
        print(*stack)
        return
    
    
    for next in array:
        if current > next:
            continue
        stack.append(next)
        dfs(next)
        stack.pop()


dfs(-1)